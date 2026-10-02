# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: worktree
- L18: Purpose
- L22: Triggers
- L29: Calls (outbound)
- L33: Called By (inbound)
- L39: Operations
- L41: Create Worktree
- L58: List Worktrees
- L66: Cleanup Worktree
- L80: Cleanup All Stale
- L91: Safety Rules
- L101: Output Format
- L104: Worktree Report
- L108: Active Worktrees
- L115: Constraints
- L123: Sharp Edges
- L132: Done When
- L140: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
