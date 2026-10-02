# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L21: scout
- L25: Instructions
- L29: Phase 1: Structure Scan
- L53: Phase 2: Targeted Search (Search-First)
- L103: Saturation
- L110: Phase 3: Dependency Mapping
- L116: Phase 4: Convention Detection
- L127: Phase 4.5: Zoom-Out Mode
- L159: Phase 5: Codebase Map (Optional)
- L166: Codebase Map
- L169: Module Boundaries
- L175: Dependency Graph (Mermaid)
- L184: Domain Ownership
- L198: Phase 6: Generate Report
- L202: Constraints
- L209: Error Recovery
- L215: Calls (outbound)
- L219: Called By (inbound)
- L248: Output Format
- L251: Scout Report
- L255: Relevant Files
- L260: Dependencies
- L263: Conventions
- L268: Search-First Assessment
- L273: Observations
- L277: Returns
- L284: Sharp Edges
- L295: Done When
- L305: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
