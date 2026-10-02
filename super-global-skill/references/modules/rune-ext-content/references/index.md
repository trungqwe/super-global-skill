# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/content
- L17: Purpose
- L21: Triggers
- L34: Skills Included
- L47: Workflows
- L59: Connections
- L76: Sharp Edges
- L89: Done When
- L96: Cost Profile

## Bundled files

- `upstream/skills/blog-patterns.md`
- `upstream/skills/cms-integration.md`
- `upstream/skills/content-scoring.md`
- `upstream/skills/i18n.md`
- `upstream/skills/mdx-authoring.md`
- `upstream/skills/reference.md`
- `upstream/skills/seo-patterns.md`
- `upstream/skills/video-repurpose.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
