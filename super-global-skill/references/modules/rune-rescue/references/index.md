# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L18: rescue
- L20: Purpose
- L30: Triggers
- L35: Calls (outbound)
- L50: Called By (inbound)
- L57: Execution
- L59: Step 0 — Initialize TodoWrite
- L77: Phase 0 — RECON
- L142: Phase 1 — SAFETY NET
- L182: Phase 2-N — SURGERY (one module per session)
- L280: Phase N+1 — CLEANUP
- L314: Phase N+2 — VERIFY
- L361: Status Command
- L366: Rescue Dashboard
- L372: Module Status
- L382: Safety Rules
- L392: Constraints
- L401: Mesh Gates
- L409: Output Format
- L412: Rescue Report: [Module Name]
- L421: Returns
- L431: Document Ownership
- L441: Anti-Patterns
- L454: Sharp Edges
- L466: Done When
- L475: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
