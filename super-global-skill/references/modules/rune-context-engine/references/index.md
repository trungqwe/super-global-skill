# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: context-engine
- L19: Purpose
- L23: Behavioral Contexts
- L37: Triggers
- L43: Calls (outbound)
- L45: Exception: L3→L3 coordination
- L48: Called By (inbound)
- L57: Execution
- L59: Step 1 — Count tool calls
- L65: Step 2 — Classify health
- L92: Step 3 — If YELLOW
- L100: Step 4 — If ORANGE
- L110: Step 5 — If RED
- L126: Step 6 — Report
- L130: Step 6b — Context Percentage Advisory
- L143: Iterative Retrieval (Context-Loading Strategy)
- L158: Compaction Technique: Structured Summary with Continuation Point
- L162: Summary Structure
- L167: Compaction Summary (generated at [tool call count])
- L169: Topics Covered
- L172: Key Decisions Made
- L175: Active Threads
- L180: Emotional/Priority Context
- L184: Continuation Point
- L188: Why This Structure
- L195: Rules
- L202: Incremental Stream Processing
- L206: Pattern: Buffer → Detect Boundary → Act
- L219: When to Use
- L225: When NOT to Use
- L231: Artifact Folding (Large Output Management)
- L235: When to Fold
- L244: Folding Procedure
- L267: Rules
- L275: Why
- L279: Context Health Levels
- L290: Output Format
- L293: Context Health
- L299: Critical Context (preserved on compaction)
- L307: Strategic Compact Decision Table
- L324: Mid-Loop Compaction (Phase 4 Emergency)
- L340: Context Budget Audit (Baseline Cost Awareness)
- L344: Token Cost Reference
- L353: Budget Rules
- L362: Audit Procedure
- L372: Report Addition
- L377: Context Budget
- L384: Output Modes
- L402: Output Density Mode (Caveman)
- L409: Activation triggers
- L419: Auto-clarity exceptions (revert ONE response, then resume)
- L427: Anti-pattern
- L431: Actionable Output Mode
- L443: Mode: preview (v1.1.0)
- L447: Why
- L451: Token Estimation (no tokenizer dep)
- L459: Threshold Defaults (per caller)
- L470: Action Enum
- L480: Signal Payload Schema
- L495: Step P1 — Receive request
- L499: Step P2 — Estimate
- L503: Step P3 — Resolve threshold
- L507: Step P4 — Determine action
- L515: Step P5 — Emit
- L521: Constraints
- L528: Sharp Edges
- L548: Done When
- L557: Cost Profile

## Bundled files

- `upstream/references/actionable-mode.md`
- `upstream/references/caveman-mode.md`
- `upstream/references/output-modes.md`
- `upstream/references/preview-gate.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
