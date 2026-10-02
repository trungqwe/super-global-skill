# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: preflight
- L19: Purpose
- L27: Triggers
- L34: Calls (outbound)
- L41: Called By (inbound)
- L45: Check Categories
- L56: Executable Steps
- L58: Stage A — Spec Compliance (Plan vs Diff)
- L78: Step 1 — Logic Review
- L110: Step 2 — Error Handling
- L139: Step 3 — Regression Check
- L148: Step 4 — Completeness Check
- L166: Step 4.2 — Coherence Check
- L184: Step 4.3 — Eval Verification
- L197: Step 4.5 — Domain Quality Hooks
- L272: Domain Quality
- L278: Step 4.6 — Organization Approval Requirements (Business)
- L301: Organization Requirements
- L312: Step 4.8 — Preflight Composite Score
- L316: Formula
- L330: Grade Thresholds
- L343: Step 5 — Security Sub-Check
- L346: Step 6 — Generate Verdict
- L368: Output Format
- L371: Preflight Report
- L377: Logic Issues
- L387: Error Handling
- L393: Regression Risk
- L396: Completeness
- L400: Coherence
- L404: Security (from sentinel)
- L407: Composite Score
- L411: Verdict
- L417: Constraints
- L425: Returns
- L435: Sharp Edges
- L451: Done When
- L462: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
