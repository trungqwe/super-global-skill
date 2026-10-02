# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/gamedev
- L17: Purpose
- L21: Triggers
- L38: Skills Included
- L55: Common Workflows
- L67: Cross-Pack Connections
- L76: Connections
- L89: Tech Stack Support
- L99: Constraints
- L110: Sharp Edges
- L125: Done When
- L142: Cost Profile

## Bundled files

- `upstream/skills/asset-pipeline.md`
- `upstream/skills/audio-system.md`
- `upstream/skills/camera-system.md`
- `upstream/skills/ecs.md`
- `upstream/skills/game-loops.md`
- `upstream/skills/input-system.md`
- `upstream/skills/multiplayer.md`
- `upstream/skills/particles.md`
- `upstream/skills/physics-engine.md`
- `upstream/skills/scene-management.md`
- `upstream/skills/threejs-patterns.md`
- `upstream/skills/webgl.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
