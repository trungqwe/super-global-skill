# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L20: launch
- L22: Purpose
- L30: Triggers
- L35: Calls (outbound)
- L48: Called By (inbound)
- L55: Execution
- L57: Step 0 — Artifact Readiness Check
- L81: Artifact Check
- L89: Step 1 — Initialize TodoWrite
- L103: Phase 1 — PRE-FLIGHT
- L132: Phase 2 — DEPLOY
- L184: Phase 3 — VERIFY LIVE
- L228: Phase 4 — MARKET
- L259: Phase 5 — ANNOUNCE
- L278: Constraints
- L286: Mesh Gates
- L294: Output Format
- L297: Launch Report
- L302: Deployment
- L307: Monitoring
- L312: Marketing Assets
- L321: Returns
- L331: Sharp Edges
- L343: Done When
- L353: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
