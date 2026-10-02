# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: asset-creator
- L17: Purpose
- L21: Called By (inbound)
- L27: Calls (outbound)
- L31: Executable Instructions
- L33: Step 1: Receive Brief
- L42: Step 2: Design
- L64: Step 3: Create
- L91: Step 4: Variants
- L99: Step 5: Report
- L104: Assets Created
- L106: Generated Files
- L111: Usage Instructions
- L117: Design Tokens Used
- L124: Note
- L128: Output Format
- L132: Constraints
- L138: Sharp Edges
- L150: Done When
- L158: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
