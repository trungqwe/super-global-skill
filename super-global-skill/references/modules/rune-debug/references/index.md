# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: debug
- L19: Purpose
- L33: Triggers
- L41: Calls (outbound)
- L54: Called By (inbound)
- L61: Cross-Hub Connections
- L66: Execution
- L68: Step 0: Build a Feedback Loop (the actual skill)
- L79: Step 1: Reproduce
- L88: Step 1.5: Scope Lock (Edit Boundary)
- L105: Step 2: Gather Evidence
- L154: Step 2b: Instrument with Preserved Markers
- L181: Step 2c: Check Debug Knowledge Base
- L190: [date] — [symptom summary]
- L199: Step 2d: Known Error Pattern Matching
- L231: Step 3: Form Hypotheses
- L242: Step 4: Test Hypotheses
- L253: Step 5: Identify Root Cause
- L261: Step 5b: Capture Error Pattern
- L265: Step 6: 3-Fix Escalation Rule
- L285: 3+ Fixes as Architectural Signal
- L300: Step 7: Report
- L308: Analysis Paralysis Guard
- L318: Hash-Based Evidence Loop Detection
- L341: Red Flags — STOP and Return to Step 2
- L356: Constraints
- L369: Output Format
- L372: Debug Report
- L379: Root Cause
- L382: Location
- L385: Evidence
- L389: Previous Fix Attempts (if any)
- L393: Concerns (if DONE_WITH_CONCERNS)
- L396: Context Needed (if NEEDS_CONTEXT)
- L399: Suggested Fix
- L403: Related Code
- L407: Status Protocol (Subagent Contract)
- L418: Returns
- L427: Chain Metadata
- L449: Sharp Edges
- L473: Done When
- L484: Cost Profile

## Bundled files

- `upstream/references/feedback-loop-ladder.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
