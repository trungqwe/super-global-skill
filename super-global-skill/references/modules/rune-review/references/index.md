# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: review
- L19: Purpose
- L28: Triggers
- L35: Calls (outbound)
- L51: Called By (inbound)
- L61: Cross-Hub Connections
- L71: Execution
- L73: Review Policy
- L83: Step 1: Scope
- L109: Step 1.5: Blast Radius Assessment
- L129: Step 1.6: Decorrelated Bug-Finding (council, high-blast-radius only)
- L154: Step 2: Logic Check (Production-Critical Focus)
- L195: Step 3: Pattern Check
- L208: Step 4: Security Check
- L221: Step 4.5: API Pit-of-Success Check
- L237: Step 4.7: API Contract / Breaking Change Check
- L261: Step 5: Test Coverage
- L289: Test Gap Analysis
- L301: Step 5.5: Two-Stage Review Gate
- L318: Spec Compliance Checklist
- L334: Step 5.7: Subtractive Pass (over-engineering lens)
- L352: Step 6: Report
- L406: Step 6.5: Fix-First Triage
- L430: Step 6.6: Scope Drift Detection
- L455: UI/UX Anti-Pattern Checks
- L591: Motion Craft Checks
- L627: Weighted Composite Scoring
- L631: Formula
- L643: Grade Thresholds
- L656: Severity Levels
- L665: Output Format
- L668: Code Review Report
- L676: Spec Compliance
- L679: CRITICAL
- L685: HIGH
- L692: MEDIUM
- L698: Blast Radius
- L701: Positive Notes
- L704: Verdict
- L707: Follow-ups (outside this scope)
- L715: Review Staleness Detection
- L726: Constraints
- L736: Returns
- L746: Chain Metadata
- L769: Sharp Edges
- L794: Done When
- L805: Cost Profile

## Bundled files

- `upstream/references/rules/config.md`
- `upstream/references/rules/default.md`
- `upstream/references/rules/go.md`
- `upstream/references/rules/index.md`
- `upstream/references/rules/python.md`
- `upstream/references/rules/rust.md`
- `upstream/references/rules/sql.md`
- `upstream/references/rules/ts-js.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
