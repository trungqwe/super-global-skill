# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: safeguard
- L17: Purpose
- L25: Called By (inbound)
- L30: Calls (outbound)
- L36: Cross-Hub Connections
- L40: Execution Steps
- L42: Step 1 — Identify module boundaries
- L52: Step 2 — Write characterization tests
- L76: Step 3 — Add boundary markers
- L94: Step 4 — Config freeze
- L108: Step 5 — Create rollback point
- L120: Step 6 — Verify
- L132: Output Format
- L135: Safeguard Report
- L144: Characterization Tests
- L147: Boundary Markers
- L152: Config Frozen
- L155: Next Step
- L159: Constraints
- L166: Sharp Edges
- L178: Done When
- L188: Returns
- L198: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
