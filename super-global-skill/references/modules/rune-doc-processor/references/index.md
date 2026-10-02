# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: doc-processor
- L17: Purpose
- L21: Triggers
- L29: Calls (outbound)
- L33: Called By (inbound)
- L40: Format Reference
- L42: Supported Formats
- L53: Library Selection
- L61: Executable Steps
- L63: Generate Mode
- L152: Parse Mode
- L185: Output Format
- L187: Generate Mode Output
- L200: Parse Mode Output
- L222: Constraints
- L231: Sharp Edges
- L241: Done When
- L243: Generate Mode
- L249: Parse Mode
- L254: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
