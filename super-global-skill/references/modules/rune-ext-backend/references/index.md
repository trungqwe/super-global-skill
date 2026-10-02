# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/backend
- L17: Purpose
- L21: Triggers
- L35: Skills Included
- L48: Tech Stack Support
- L59: Connections
- L78: Sharp Edges
- L91: Done When
- L104: Cost Profile

## Bundled files

- `upstream/skills/api-patterns.md`
- `upstream/skills/async-pipeline.md`
- `upstream/skills/auth-patterns.md`
- `upstream/skills/background-jobs.md`
- `upstream/skills/caching-patterns.md`
- `upstream/skills/cli-generation.md`
- `upstream/skills/database-patterns.md`
- `upstream/skills/middleware-patterns.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
