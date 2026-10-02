# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/devops
- L17: Purpose
- L21: Triggers
- L36: Skills Included
- L50: Tech Stack Support
- L63: Connections
- L78: Sharp Edges
- L89: Done When
- L101: Cost Profile

## Bundled files

- `upstream/skills/chaos-testing.md`
- `upstream/skills/ci-cd.md`
- `upstream/skills/docker.md`
- `upstream/skills/edge-serverless.md`
- `upstream/skills/infra-as-code.md`
- `upstream/skills/kubernetes.md`
- `upstream/skills/monitoring.md`
- `upstream/skills/server-setup.md`
- `upstream/skills/ssl-domain.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
