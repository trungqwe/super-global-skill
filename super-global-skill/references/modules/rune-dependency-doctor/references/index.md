# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: dependency-doctor
- L17: Purpose
- L21: Called By (inbound)
- L26: Calls (outbound)
- L30: Executable Instructions
- L32: Step 1: Detect Package Manager
- L50: Step 2: List Dependencies
- L59: Step 3: Check Outdated
- L98: Step 4: Check Vulnerabilities
- L135: Step 5: Analyze Breaking Changes
- L144: Step 6: Generate Update Plan
- L161: Step 7: Report
- L166: Dependency Report: [project name]
- L173: Critical — CVEs (Fix Immediately)
- L177: Security — CVEs (Fix This Sprint)
- L180: Outdated — Patch (Safe to Update)
- L183: Outdated — Minor (Update with Testing)
- L186: Outdated — Major (Plan Migration)
- L189: Unused Dependencies
- L192: Update Plan (Ordered by Risk)
- L197: Dependency Health Score
- L203: Upgrade Campaign Mode
- L207: Campaign Chain
- L228: Calls (outbound — Campaign Mode only)
- L233: Output Format
- L237: Constraints
- L244: Sharp Edges
- L255: Done When
- L265: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
