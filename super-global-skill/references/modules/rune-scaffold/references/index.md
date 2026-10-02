# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: scaffold
- L17: Purpose
- L25: Triggers
- L32: Calls (outbound)
- L48: Called By (inbound)
- L54: Modes
- L56: Interactive Mode (default)
- L65: Express Mode
- L79: Project Templates
- L93: Executable Steps
- L95: Phase 1 — BA (Requirement Elicitation)
- L107: Phase 2 — RESEARCH (Best Practices & Templates)
- L117: Phase 3 — PLAN (Architecture & Implementation)
- L130: Phase 4 — DESIGN (Design System — Frontend Only)
- L138: Phase 5 — IMPLEMENT (Code Generation)
- L158: Phase 6 — TEST (Test Suite Generation)
- L169: Phase 7 — DOCS (Documentation)
- L178: Phase 8 — GIT (Initial Commit)
- L186: Phase 9 — VERIFY (Quality Gate)
- L202: Output Format
- L205: Scaffold Report: [Project Name]
- L213: Generated Structure
- L216: What's Included
- L219: What's NOT Included (Next Steps)
- L222: Commands
- L229: Error Recovery
- L241: Monorepo Mode
- L245: Monorepo Detection & Setup
- L251: Structure Generated
- L265: Monorepo-Specific Steps (additions to standard scaffold)
- L274: Monorepo Anti-Patterns
- L281: Constraints
- L294: Returns
- L304: Sharp Edges
- L316: Done When
- L328: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
