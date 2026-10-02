# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/analytics
- L17: Purpose
- L21: Triggers
- L31: Skills Included
- L43: Tech Stack Support
- L52: Connections
- L61: Constraints
- L69: Sharp Edges
- L80: Done When
- L92: Cost Profile

## Bundled files

- `upstream/skills/ab-testing.md`
- `upstream/skills/dashboard-patterns.md`
- `upstream/skills/data-validation.md`
- `upstream/skills/funnel-analysis.md`
- `upstream/skills/sql-patterns.md`
- `upstream/skills/statistical-analysis.md`
- `upstream/skills/tracking-setup.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
