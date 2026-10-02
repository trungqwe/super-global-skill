# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: constraint-check
- L18: Purpose
- L24: Triggers
- L31: Calls (outbound)
- L35: Called By (inbound)
- L42: Execution
- L44: Step 1 — Identify Active Skills
- L55: Step 2 — Load Constraint Definitions
- L68: Step 3 — Audit Compliance
- L81: Step 4 — Classify Violations
- L89: Step 5 — Report
- L92: Constraint Check Report
- L98: HARD-GATE Violations (BLOCK)
- L102: Constraint Violations (WARN)
- L106: Compliance Summary
- L114: Remediation
- L119: Constraint Catalog (Quick Reference)
- L135: Output Format
- L139: Constraints
- L147: Sharp Edges
- L156: Done When
- L165: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
