# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: db
- L18: Purpose
- L22: Triggers
- L29: Calls (outbound)
- L35: Called By (inbound)
- L41: References
- L45: Executable Steps
- L47: Step 1 — Discovery
- L57: Step 2 — Diff Analysis
- L65: Step 3 — Breaking Change Detection
- L89: Step 4 — Migration Generation
- L110: NEVER leave downgrade() empty — HARD-GATE blocks this
- L135: Step 5 — Index Analysis
- L145: Step 6 — Query Parameterization Scan
- L150: BAD: string interpolation in SQL
- L153: GOOD: parameterized
- L160: Step 7 — Schema Documentation
- L165: [date] — [migration name]
- L172: Step 8 — Report
- L177: DB Report: [scope]
- L179: Schema Changes
- L182: Breaking Changes Requiring Confirmation
- L185: Generated Files
- L188: Index Recommendations
- L191: Query Safety
- L195: Verdict: PASS | WARN | BLOCK
- L198: Output Format
- L201: DB Report: schema.prisma diff
- L203: Schema Changes
- L207: Breaking Changes Requiring Confirmation
- L212: Generated Files
- L215: Index Recommendations
- L218: Verdict: BLOCK (breaking change unconfirmed)
- L221: Constraints
- L229: Mesh Gates (L1/L2 only)
- L238: Sharp Edges
- L250: Done When
- L261: Returns
- L271: Cost Profile

## Bundled files

- `upstream/references/scaling-reference.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
