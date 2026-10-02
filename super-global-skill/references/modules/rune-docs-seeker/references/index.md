# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L19: docs-seeker
- L21: Purpose
- L25: Calls (outbound)
- L29: Called By (inbound)
- L36: Execution
- L38: Input
- L46: Step 1 — Identify Target
- L53: Step 2 — Try Context7 MCP (fastest)
- L62: Step 3 — Try llms.txt Discovery
- L88: Step 4 — Fallback to Web Search
- L105: Step 5 — Extract Answer
- L113: Step 6 — Report
- L117: Constraints
- L126: Output Format
- L129: Documentation: [Library/API]
- L133: API Reference
- L140: Usage Example
- L145: Known Issues / Deprecations
- L149: Sharp Edges
- L161: Done When
- L171: Returns
- L180: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
