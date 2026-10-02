# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: mcp-builder
- L17: Purpose
- L21: Triggers
- L28: Calls (outbound)
- L36: Called By (inbound)
- L42: Executable Steps
- L44: Step 1 — Spec Elicitation
- L57: Step 2 — Architecture Design
- L110: Step 3 — Generate Server Code
- L158: Required
- L162: Optional
- L181: Step 3.5 — Tool Safety Classification
- L227: Step 4 — Generate Tests
- L256: Step 5 — Generate Documentation
- L281: Step 6 — Verify
- L289: Output Format
- L291: Generated Project Structure
- L322: README Structure
- L328: Reference Pattern: Multi-Provider Adapter
- L332: Interface
- L343: Discriminated Union for Stream Chunks
- L355: When to Apply
- L361: Key Implementation Notes
- L368: Cost-Aware Model Selection
- L380: Constraints
- L390: Sharp Edges
- L402: Done When
- L412: Returns
- L423: Cost Profile

## Bundled files

- `upstream/references/auto-discovery-pattern.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
