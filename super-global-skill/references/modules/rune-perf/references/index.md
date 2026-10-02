# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: perf
- L17: Purpose
- L21: Triggers
- L29: Calls (outbound)
- L36: Called By (inbound)
- L44: References
- L52: Executable Steps
- L54: Step 1 — Scope
- L61: Step 2 — DB Query Patterns
- L67: BAD: N+1
- L71: GOOD: prefetch
- L78: BAD
- L81: GOOD
- L89: Step 3 — Async/Sync Violations
- L116: Step 4 — Memory Leak Patterns
- L138: BAD: unbounded cache
- L171: Step 5 — Bundle Analysis (frontend only)
- L217: Step 5.5 — Motion / Animation Performance (frontend only)
- L227: Step 6 — Framework-Specific Checks
- L249: Step 7 — Benchmark Execution
- L257: Step 8 — Report
- L262: Perf Report: [scope]
- L264: BLOCK (must fix before merge)
- L267: WARN (should fix)
- L270: PASS
- L275: Lighthouse (if ran)
- L282: Verdict: PASS | WARN | BLOCK
- L285: Step 8.5 — Token Budget Tracking (AI-Powered Apps)
- L318: Step 8.6 — Observability Cost Control
- L342: Cost Impact Hierarchy
- L381: Output Format
- L384: Perf Report: src/api/users.ts, src/db/queries.ts
- L386: BLOCK
- L389: WARN
- L392: PASS
- L396: Verdict: BLOCK
- L399: Constraints
- L407: Mesh Gates (L1/L2 only)
- L415: Sharp Edges
- L431: Done When
- L440: Returns
- L449: Cost Profile

## Bundled files

- `upstream/references/cost-reference.md`
- `upstream/references/scalability-reference.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
