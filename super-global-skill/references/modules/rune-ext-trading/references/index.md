# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/trading
- L17: Purpose
- L21: Triggers
- L28: Skills Included
- L40: Tech Stack Support
- L51: Connections
- L60: Sharp Edges
- L71: Done When
- L80: Cost Profile

## Bundled files

- `upstream/skills/chart-components.md`
- `upstream/skills/experiment-loop.md`
- `upstream/skills/fintech-patterns.md`
- `upstream/skills/indicator-library.md`
- `upstream/skills/quant-analysis.md`
- `upstream/skills/realtime-data.md`
- `upstream/skills/trade-logic.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
