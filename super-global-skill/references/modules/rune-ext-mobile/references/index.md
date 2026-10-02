# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/mobile
- L17: Purpose
- L21: Triggers
- L36: Skills Included
- L52: Connections
- L71: Tech Stack Support
- L80: Sharp Edges
- L95: Done When
- L106: Cost Profile

## Bundled files

- `upstream/skills/app-store-connect.md`
- `upstream/skills/app-store-prep.md`
- `upstream/skills/deep-linking.md`
- `upstream/skills/flutter.md`
- `upstream/skills/ios-build-pipeline.md`
- `upstream/skills/native-bridge.md`
- `upstream/skills/ota-updates.md`
- `upstream/skills/push-notifications.md`
- `upstream/skills/react-native.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
