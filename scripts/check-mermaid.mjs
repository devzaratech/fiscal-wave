import fs from "node:fs/promises";
import path from "node:path";
import mermaid from "mermaid";

const dir = process.argv[2];
if (!dir) {
  console.error("Usage: node check-mermaid.mjs <generated-mermaid-directory>");
  process.exit(2);
}
mermaid.initialize({ startOnLoad: false, securityLevel: "strict" });
const files = (await fs.readdir(dir)).filter((file) => file.endsWith(".mmd")).sort();
if (files.length === 0) {
  console.error("No Mermaid diagrams found.");
  process.exit(1);
}
let errors = 0;
for (const filename of files) {
  const source = await fs.readFile(path.join(dir, filename), "utf8");
  try {
    const parsed = await mermaid.parse(source, { suppressErrors: false });
    if (!parsed) throw new Error("Mermaid parser returned no diagram");
    console.log("PASS " + filename + " (" + parsed.diagramType + ")");
  } catch (err) {
    errors++;
    console.error("FAIL " + filename + ": " + (err?.message ?? String(err)));
  }
}
if (errors > 0) process.exit(1);
console.log("All " + files.length + " Mermaid diagrams parsed.");
