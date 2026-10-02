# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: plan
- L19: Purpose
- L45: Architecture: Master Plan + Phase Files
- L55: Why This Architecture
- L63: Size Constraints
- L71: Modes
- L73: Implementation Mode (default)
- L76: Feature Spec Mode
- L80: Roadmap Mode
- L84: Triggers
- L93: Calls (outbound)
- L103: Called By (inbound)
- L116: Data Flow
- L118: Feeds Into →
- L125: Fed By ←
- L132: Feedback Loops ↻
- L137: Executable Steps (Implementation Mode)
- L139: Step 1 — Gather Context
- L149: Step 2 — Classify Complexity
- L163: Step 3 — Decompose into Phases
- L188: Step 3.7 — Boundary Artifacts (Contracts-First)
- L207: Step 4 — Write Master Plan File
- L212: Step 4.5 — Workflow Registry (Complex Features Only)
- L219: Step 5 — Write Phase Files
- L240: Step 5.5 — Completeness Scoring (Alternatives)
- L245: Step 5.7 — Coverage Gate (after phase files, before presenting)
- L252: Coverage Summary
- L271: Step 6 — Present and Get Approval
- L275: Step 6.5 — Update Feature Map (Always)
- L294: Step 7 — Execution Handoff
- L307: Inline Plan (Trivial Tasks)
- L311: Re-Planning (Dynamic Adaptation)
- L323: Feature Spec Mode
- L333: Roadmap Mode
- L340: Output Format
- L348: Outcome Block (Mandatory)
- L353: Change Stacking (Overlap Detection)
- L358: Task: Implement auth middleware
- L377: Constraints
- L397: Returns
- L411: Chain Metadata
- L441: Sharp Edges
- L476: Self-Validation
- L493: Done When
- L514: Cost Profile

## Bundled files

- `upstream/references/boundary-artifacts.md`
- `upstream/references/completeness-scoring.md`
- `upstream/references/feature-map.md`
- `upstream/references/outcome-block.md`
- `upstream/references/plan-templates.md`
- `upstream/references/vertical-slice.md`
- `upstream/references/wave-planning.md`
- `upstream/references/workflow-registry.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
