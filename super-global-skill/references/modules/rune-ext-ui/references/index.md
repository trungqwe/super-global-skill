# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/ui
- L19: Purpose
- L30: Triggers
- L47: Skills Included
- L62: Tech Stack Support
- L72: Connections
- L92: Constraints
- L102: Sharp Edges
- L117: Done When
- L130: Cost Profile

## Bundled files

- `upstream/skills/a11y-audit.md`
- `upstream/skills/animation-patterns.md`
- `upstream/skills/component-patterns.md`
- `upstream/skills/design-decision.md`
- `upstream/skills/design-system.md`
- `upstream/skills/landing-patterns.md`
- `upstream/skills/palette-picker.md`
- `upstream/skills/react-health.md`
- `upstream/skills/type-system.md`
- `upstream/skills/web-vitals.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
