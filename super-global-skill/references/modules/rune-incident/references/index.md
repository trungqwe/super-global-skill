# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: incident
- L19: Purpose
- L23: Triggers
- L30: Calls (outbound)
- L38: Called By (inbound)
- L44: Executable Steps
- L46: Step 1 — Triage
- L62: Step 2 — Contain
- L84: Step 3 — Verify Containment
- L91: Step 4 — Security Check
- L102: Step 5 — Root Cause Analysis
- L113: Step 6 — Timeline Construction
- L134: Step 7 — Postmortem
- L139: Incident Report: [title]
- L146: Timeline
- L149: Root Cause
- L152: Contributing Factors
- L155: What Went Well
- L158: What Went Wrong
- L161: Prevention Actions
- L167: Lessons Learned
- L171: Output Format
- L174: Incident Response: [title]
- L176: Triage
- L179: Containment
- L183: Security Check
- L186: Root Cause (from autopsy)
- L191: Timeline
- L200: Postmortem saved
- L204: Constraints
- L213: Mesh Gates (L1/L2 only)
- L222: Returns
- L232: Sharp Edges
- L244: Done When
- L254: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
