# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: completion-gate
- L18: Purpose
- L29: Triggers
- L36: Calls (outbound)
- L40: Called By (inbound)
- L45: Execution
- L47: Step 1 — Collect Claims
- L63: Step 1a — Type Each Claim (Claim Discipline)
- L90: Step 1b — Stub Detection (Existence Theater Check)
- L105: Step 1c — Self-Validation Check
- L123: Step 1d — Execution Loop Audit
- L147: Step 2 — Match Evidence
- L161: Step 3 — Validate Each Claim (Default-FAIL Mindset)
- L200: Step 4 — Report
- L203: Completion Gate Report
- L208: Claim Validation
- L216: Gaps (if any)
- L220: Open (declared, not failures)
- L223: Verdict
- L227: Step 4.5 — Integration Check (Cross-Phase + Cross-Layer)
- L262: Step 5 — Evidence Quality Gate
- L279: Step 5.5 — Plan Diff Check
- L302: Verdict Rules
- L311: Output Format
- L315: Constraints
- L323: Sharp Edges
- L342: Done When
- L352: Cost Profile

## Bundled files

- `upstream/references/claim-discipline.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
