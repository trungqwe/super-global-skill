# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L20: team
- L22: Purpose
- L32: Triggers
- L37: Mode Selection (Auto-Detect)
- L46: Lite Mode
- L70: Full Mode
- L74: Complexity Tiers (DAG Stage Selection)
- L94: Calls (outbound)
- L98: Exception: L1→L1 meta-orchestration (team is the only L1 that calls other L1s)
- L110: Called By (inbound)
- L117: Execution
- L119: Step 0 — Initialize TodoWrite
- L133: Phase 1 — DECOMPOSE
- L215: Phase 2 — ASSIGN
- L240: NEXUS Handoff: Stream [id]
- L242: Metadata
- L248: Context
- L254: Deliverable
- L259: Quality Expectations
- L265: Evidence Required
- L314: Phase 3 — COORDINATE
- L386: Phase 4 — MERGE
- L393: Bookmark before any merge
- L425: Phase 5 — VERIFY
- L450: Constraints
- L459: Mesh Gates
- L467: Output Format
- L470: Team Report: [Task Name]
- L475: Streams
- L482: Acceptance Criteria
- L489: Integration
- L498: Parallel Execution Rules
- L506: Returns
- L516: Document Ownership
- L526: Monorepo Awareness
- L544: Anti-Patterns
- L557: Sharp Edges
- L578: Done When
- L587: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
