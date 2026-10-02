# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: scope-guard
- L18: Purpose
- L22: Called By (inbound)
- L29: Calls (outbound)
- L33: Executable Instructions
- L35: Step 1: Load Plan
- L48: Step 2: Assess Current Work
- L64: Step 3: Compare
- L81: Step 4: Quantify Drift
- L104: Step 5: Report
- L109: Scope Report
- L117: In-Scope Changes
- L120: Out-of-Scope Changes
- L123: Recommendations
- L130: Output Format
- L133: Scope Report
- L137: Out-of-Scope Changes
- L141: Recommendations
- L146: Constraints
- L152: Sharp Edges
- L164: Done When
- L172: Returns
- L181: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
