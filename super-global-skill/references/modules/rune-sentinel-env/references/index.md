# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: sentinel-env
- L17: Purpose
- L23: Triggers
- L31: Calls (outbound)
- L35: Called By (inbound)
- L43: Data Flow
- L45: Feeds Into →
- L49: Execution
- L51: Step 1: Detect Project Type
- L73: Step 2: Runtime Version Check
- L78: Node.js
- L81: or pnpm/yarn/bun depending on lockfile present
- L83: Python
- L87: Rust
- L91: Go
- L94: Docker
- L105: Step 3: Required Tools Check
- L161: Step 4: Port Availability Check
- L180: Step 5: Environment Variables Check
- L193: Step 6: Disk Space and System Resources
- L206: Step 6.6: AI-Agent Fleet Detection (opt-in — `--agents` flag, or when called by `council`)
- L218: Step 7: Report
- L229: Output Format
- L232: Environment Check: [project name]
- L237: BLOCKED
- L241: WARNINGS
- L247: PASSED
- L253: AI AGENTS (only when --agents / council mode ran)
- L260: Constraints
- L269: Sharp Edges
- L284: Done When
- L295: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
