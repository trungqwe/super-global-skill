# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/chrome-ext
- L17: Purpose
- L21: Triggers
- L30: Skills Included
- L41: Tech Stack Support
- L58: Connections
- L70: Sharp Edges
- L81: Done When
- L93: Cost Profile

## Bundled files

- `upstream/skills/cws-preflight.md`
- `upstream/skills/cws-publish.md`
- `upstream/skills/ext-ai-integration.md`
- `upstream/skills/ext-messaging.md`
- `upstream/skills/ext-storage.md`
- `upstream/skills/mv3-scaffold.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
