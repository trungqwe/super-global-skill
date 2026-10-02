# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L20: @rune/saas
- L22: Purpose
- L26: Triggers
- L37: Skills Included
- L48: Workflows
- L56: Tech Stack Support
- L73: Connections
- L86: Sharp Edges
- L105: Done When
- L116: Cost Profile

## Bundled files

- `upstream/skills/billing-integration.md`
- `upstream/skills/feature-flags.md`
- `upstream/skills/multi-tenant.md`
- `upstream/skills/onboarding-flow.md`
- `upstream/skills/subscription-flow.md`
- `upstream/skills/team-management.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
