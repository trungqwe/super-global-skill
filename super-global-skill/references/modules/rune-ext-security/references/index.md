# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L21: @rune/security
- L23: Purpose
- L27: Triggers
- L35: Skills Included
- L47: Connections
- L58: Constraints
- L66: Sharp Edges
- L81: Difference from sentinel
- L89: Done When
- L99: Cost Profile

## Bundled files

- `upstream/skills/api-security.md`
- `upstream/skills/compliance.md`
- `upstream/skills/defense-in-depth.md`
- `upstream/skills/owasp-audit.md`
- `upstream/skills/pentest-patterns.md`
- `upstream/skills/secret-mgmt.md`
- `upstream/skills/supply-chain.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
