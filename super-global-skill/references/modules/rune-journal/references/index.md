# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: journal
- L18: Purpose
- L22: Triggers
- L27: Calls (outbound)
- L31: Called By (inbound)
- L46: Files Managed
- L56: Execution
- L58: Step 1 — Load state
- L74: Step 2 — Update progress
- L89: Step 3 — Record decisions (gated by 3-criteria scoring)
- L118: ADR-[NNN]: [Decision Title]
- L126: Context
- L129: Decision
- L132: Rationale
- L135: Consequences
- L138: Rejected Alternatives (counter-test — MUST have at least one)
- L144: Step 3.5 — Record risks
- L152: RISK-[NNN]: [Risk Title]
- L160: Description
- L163: Impact
- L166: Mitigation
- L171: Trigger Conditions
- L174: Contingency
- L188: Step 4 — Update dependency graph
- L200: Step 5 — Save state
- L210: Step 6 — Report
- L214: Output Format
- L217: Journal Update
- L227: Context Recovery (new session)
- L238: Constraints
- L245: Sharp Edges
- L259: Done When
- L269: Cost Profile

## Bundled files

- `upstream/references/adr-criteria.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
