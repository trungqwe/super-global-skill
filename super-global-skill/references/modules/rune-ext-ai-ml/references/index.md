# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/ai-ml
- L17: Purpose
- L21: Triggers
- L35: Skills Included
- L50: Connections
- L70: Sharp Edges
- L81: Done When
- L88: Cost Profile

## Bundled files

- `upstream/skills/ai-agents.md`
- `upstream/skills/code-sandbox.md`
- `upstream/skills/deep-research.md`
- `upstream/skills/embedding-search.md`
- `upstream/skills/fine-tuning-guide.md`
- `upstream/skills/llm-architect.md`
- `upstream/skills/llm-integration.md`
- `upstream/skills/prompt-patterns.md`
- `upstream/skills/rag-patterns.md`
- `upstream/skills/web-extraction.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
