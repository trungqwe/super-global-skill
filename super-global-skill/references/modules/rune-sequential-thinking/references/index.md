# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: sequential-thinking
- L17: Purpose
- L21: Calls (outbound)
- L25: Called By (inbound)
- L31: When to Use
- L41: Execution
- L43: Input
- L52: Step 0 — Reversibility Classification
- L64: Step 1 — Identify All Variables
- L73: Step 2 — Map Dependencies
- L84: Step 3 — Evaluate in Dependency Order
- L105: Step 4 — Second-Order Effects Check
- L123: Step 5 — Bias Cross-Check
- L135: Step 6 — Synthesize
- L143: Step 7 — Report
- L147: Constraints
- L157: Output Format
- L160: Sequential Analysis: [Decision]
- L162: Reversibility: [two-way door / one-way door / partially reversible]
- L165: Variables Identified
- L171: Dependency Map
- L175: Step-by-Step Evaluation
- L190: Second-Order Effects (one-way door only)
- L195: Bias Check
- L198: Ambiguities
- L201: Final Recommendation
- L209: Sharp Edges
- L222: Done When
- L234: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
