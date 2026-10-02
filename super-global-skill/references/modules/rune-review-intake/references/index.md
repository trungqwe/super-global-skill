# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: review-intake
- L19: Purpose
- L23: Modes
- L32: Triggers
- L41: Calls (outbound)
- L49: Called By (inbound)
- L54: Workflow (PR Review Mode)
- L59: Phase 1 — ABSORB
- L73: Phase 2 — COMPREHEND
- L85: Phase 3 — VERIFY
- L100: Phase 4 — EVALUATE
- L114: Reviewer says "implement this properly"
- L115: First: is anyone actually using it?
- L117: Zero results? → "This isn't called anywhere. Remove it (YAGNI)?"
- L120: Phase 5 — RESPOND
- L159: Phase 4.5 — Rejection KB Write (when verdict = OUT OF SCOPE)
- L177: Phase 6 — IMPLEMENT
- L187: Source Trust Levels
- L198: Pushback Framework
- L213: Output Format
- L216: Review Intake Report
- L218: Summary
- L222: Verdicts
- L229: Changes Applied
- L232: Verification
- L237: Constraints
- L246: Mesh Gates
- L254: Sharp Edges
- L271: Done When
- L281: Returns
- L290: Cost Profile

## Bundled files

- `upstream/references/issue-triage.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
