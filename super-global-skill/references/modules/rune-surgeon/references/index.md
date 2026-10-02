# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: surgeon
- L17: Purpose
- L28: Called By (inbound)
- L33: Calls (outbound)
- L44: Consuming proposal payloads
- L57: Execution Steps
- L59: Step 1 — Pre-surgery scan
- L76: Step 2 — Select refactoring pattern
- L89: Step 3 — Refactor
- L108: Step 4 — Test after each change
- L121: Step 5 — Review
- L127: Step 6 — Commit
- L138: Step 7 — Update journal
- L147: Refactoring Patterns
- L156: Safety Rules
- L167: Output Format
- L170: Surgery Report: [Module Name]
- L177: Steps Taken
- L180: Remaining (if partial)
- L184: Next Step
- L189: Constraints
- L197: Sharp Edges
- L209: Done When
- L220: Returns
- L230: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
