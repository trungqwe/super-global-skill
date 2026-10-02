# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: watchdog
- L19: Purpose
- L23: Called By (inbound)
- L29: Calls (outbound)
- L33: Executable Instructions
- L35: Step 1: Receive Target
- L43: Step 2: Health Check
- L57: Step 3: Response Time
- L70: Step 4: Performance Signal Analysis
- L82: Step 5: Error Detection
- L92: Step 6: Report
- L97: Watchdog Report: [base_url]
- L99: Smoke Test Results
- L102: Alert Rules Applied
- L108: Alerts
- L111: Performance Signals
- L114: Summary
- L124: Output Format
- L127: Watchdog Report: [base_url]
- L128: Smoke Test Results
- L133: Alerts
- L136: Summary
- L141: Constraints
- L149: Sharp Edges
- L160: Done When
- L168: Cost Profile

## Bundled files

- `upstream/references/webhook-health-checks.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
