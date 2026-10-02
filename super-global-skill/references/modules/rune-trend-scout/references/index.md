# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: trend-scout
- L17: Purpose
- L21: Calls (outbound)
- L25: Called By (inbound)
- L32: Execution
- L34: Input
- L42: Step 1 — Define Scope
- L49: Step 2 — Search Trends
- L59: Step 3 — Competitor Analysis
- L72: Step 4 — Community Sentiment
- L85: Step 5 — Report
- L89: Constraints
- L96: Output Format
- L99: Trend Report: [Topic]
- L103: Trending Now
- L107: Competitors
- L113: Community Sentiment
- L118: Emerging Patterns
- L121: Recommendations
- L125: Sharp Edges
- L136: Done When
- L145: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
