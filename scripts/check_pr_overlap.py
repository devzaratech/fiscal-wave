#!/usr/bin/env python3
"""Detect same-file changes across open PRs. Read-only API, not an atomic Git lock."""
import json
import os
import sys
import urllib.error
import urllib.request


def changed_paths(files):
    names = set()
    for f in files:
        if not isinstance(f, dict) or not isinstance(f.get("filename"), str):
            continue
        names.add(f["filename"])
        if f.get("status") == "renamed" and isinstance(f.get("previous_filename"), str):
            names.add(f["previous_filename"])
    return names


def collisions(current_paths, other_pr_file_lists):
    """Pure helper: list (pr_number, sorted shared paths)."""
    results = []
    for number, files in other_pr_file_lists:
        overlap = sorted(current_paths & changed_paths(files))
        if overlap:
            results.append((number, overlap))
    return results


def api_pages(path, token, repository):
    """Fetch all result pages; no URLs outside GitHub API."""
    if not repository or repository.count("/") != 1:
        raise ValueError("GITHUB_REPOSITORY must be owner/repo")
    result = []
    page = 1
    while True:
        url = ("https://api.github.com/repos/" + repository + "/" +
               path + ("&" if "?" in path else "?") + "per_page=100&page=" + str(page))
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + token,
            "User-Agent": "FiscalWave-PR-Overlap-Guard",
            "X-GitHub-Api-Version": "2022-11-28"
        })
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.load(response)
        if not isinstance(data, list):
            raise ValueError("Unexpected GitHub API response")
        result.extend(data)
        if len(data) < 100:
            return result
        page += 1
        if page > 20:
            raise ValueError("Too many PR pages for bounded overlap guard")


def main():
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    pr_value = os.getenv("CURRENT_PR")
    if not token or not repo or not pr_value:
        print("Missing PR context / Falta contexto del PR", file=sys.stderr)
        return 1
    try:
        current_number = int(pr_value)
        if current_number < 1:
            raise ValueError("invalid pull request number")
        pulls = api_pages("pulls?state=open", token, repo)
        current = next((p for p in pulls if p.get("number") == current_number), None)
        if current is None:
            raise ValueError("current PR not found among open PRs")
        base = current.get("base", {}).get("ref")
        current_paths = changed_paths(api_pages(f"pulls/{current_number}/files", token, repo))
        comparisons = []
        for pull in pulls:
            number = pull.get("number")
            if number == current_number or pull.get("base", {}).get("ref") != base:
                continue
            comparisons.append((number, api_pages(f"pulls/{number}/files", token, repo)))
        duplicates = collisions(current_paths, comparisons)
        if duplicates:
            for number, files in duplicates:
                print(f"Overlapping PR #{number}: " + ", ".join(files), file=sys.stderr)
            print("Coordinate the shared files before integration / Resolver solapamientos", file=sys.stderr)
            return 1
        print(f"No overlapping paths across {len(comparisons)} other open PRs / Sin rutas compartidas")
        return 0
    except (ValueError, KeyError, urllib.error.URLError, TimeoutError) as ex:
        print("Unable to verify PR collisions (fail closed): " + str(ex), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
