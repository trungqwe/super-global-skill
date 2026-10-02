# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: logic-guardian
- L18: Purpose
- L22: Triggers
- L29: Calls (outbound connections)
- L37: Called By (inbound connections)
- L45: Workflow
- L47: Phase 0 — Load Manifest + Invariants
- L65: Phase 1 — Validate Manifest Against Codebase
- L78: Phase 2 — Pre-Edit Gate (called by fix/surgeon/cook)
- L107: Phase 3 — Generate Manifest (first-time or rescan)
- L127: Phase 4 — Post-Edit Validation
- L140: Phase 5 — Cross-Session Handoff
- L153: Output Format
- L155: Manifest Schema (`.rune/logic-manifest.json`)
- L197: Validation Report
- L200: Logic Guardian Report
- L202: Manifest Status: SYNCED | DRIFT_DETECTED
- L206: Pre-Edit Gate
- L213: Post-Edit Validation
- L221: Constraints
- L230: Mesh Gates
- L238: Sharp Edges
- L249: Done When
- L258: Returns
- L267: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
