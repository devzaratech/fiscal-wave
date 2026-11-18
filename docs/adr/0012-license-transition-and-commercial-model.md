# ADR-0012 — Community licensing transition and commercial distribution / Licenciamiento Community y distribución comercial

**Status / Estado:** Proposed / Propuesto · 2026-11-18 · [FW-034](https://github.com/devzaratech/fiscal-wave/issues/21)

## Context / Contexto
FiscalWave's public `main` originally carried Apache-2.0. The product is at the architecture/documentation stage, with no Java fiscal engine in the reviewed base commit `95315c0204394e00ad3852ac04daa2667d4d0dc7`. The owner wants a fully functional Community edition with publicly visible source code, free within permitted noncommercial use, paid authorization for uses outside those grants, and optional proprietary Enterprise capabilities. / La implementación tributaria Java aún no está publicada en la línea base revisada; el modelo de negocio requiere distinguir uso comunitario, comercial y capacidades privadas.

## Decision / Decisión
1. **Community:** propose adopting the **unmodified PolyForm Noncommercial License 1.0.0** for future releases of material the licensor is entitled to license; provide its official text in root `LICENSE` and `Required Notice:` naming the current licensor as recorded in this repository (`devzaratech`). It is **source-available, not OSI-approved Open Source**. / Licencia PolyForm sin alterar; no presentarla como software Open Source.
2. **Commercial:** uses not permitted by the PolyForm terms require an **independently negotiated written commercial license** from the rights holder. No public GitHub file automatically grants commercial rights; no fee schedule or contract is published yet. / Licencia comercial separada pendiente de contrato.
3. **Enterprise:** optional advanced components may be distributed under private proprietary terms and separate service/SLA arrangements. Do not imply a released Enterprise product. / Componentes privados futuros, no una versión ya disponible.
4. **Community completeness:** no artificial disabling of core lawful tax-document functionality solely to sell Enterprise. Paid value can include alternative commercial-use permission, enterprise operations, integrations and support. / Núcleo comunitario funcional, sin bloqueos artificiales.
5. **Historic Apache 2.0:** previously distributed versions and rights validly granted under Apache-2.0 are **not retroactively withdrawn**. Preserve Git history, baseline link and attribution; the change applies to applicable newly licensed publication versions from the transition commit forward. / Conservar derechos históricos, no reescribir Git.
6. **Rights and contributions:** third-party assets retain their own licenses. Audit provenance before importing legacy ROOSTER/NicDTE materials, libraries, schemas, generated content or external contributions. Do not merge third-party PRs until rights adequate for the intended multi-license model are reviewed and documented; decide CLA/DCO separately. / Verificar titularidad y contribuciones antes de relicenciar.
7. **Governance:** create branch/PR for review; do not merge without explicit owner approval; commercial agreement, tax warranties, company/licensor legal identity and relevant Chilean/international legal treatment require professional review before commercial launch. / Revisión humana y jurídica antes de comercializar.

## PolyForm boundaries / Límites PolyForm
The license permits any noncommercial purpose, personal experiment/study (subject to its conditions), and expressly allows use by specified educational, charitable, public research, public safety/health, environmental and government institutions **regardless of funding**. We accept those standardized exceptions; there is no additional prohibition written into the PolyForm text. Refer to the actual license for enforceable terms. / Las excepciones institucionales son parte integral de la licencia elegida.

## Alternatives / Alternativas
- Keep Apache-2.0: simpler and OSI-approved, but allows proprietary commercial derivatives; rejected for future owner-controlled code.
- AGPLv3 plus commercial dual license: copyleft, but compliant commercial use remains free; does not meet blanket commercial authorization strategy.
- Custom noncommercial license: more control but unnecessary legal drafting risk at this stage.
- PolyForm with edits: rejected; use the official text without alteration.

## Evidence, transition and rollback / Evidencia, transición y reversión
- Official terms: https://polyformproject.org/licenses/noncommercial/1.0.0
- Base commit with Apache-2.0: https://github.com/devzaratech/fiscal-wave/blob/95315c0204394e00ad3852ac04daa2667d4d0dc7/LICENSE
- No force push, no removal of past grants. Effective `main` transition commit to be recorded *after* an approved merge. Until then `main` stays Apache-2.0; this PR is a proposal.
- Rollback prior to merge: close PR; after merge, a new version may adopt different terms only for code controlled by the licensor; old grants remain.

## Follow-up / Próximos pasos
- Resolve confirmed legal licensor name/entity and a confidential commercial contact channel.
- Obtain professional review of the commercial license and IP chain of title before selling.
- Establish an external-contribution agreement strategy before accepting community patches.
- Record merge commit SHA and date in licensing history after review; verify license-detection and docs checks.

**Scope:** policy/documentation only, no software deployment or legal contract execution. / Solo propuesta documental.
