# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: docs
- L18: Purpose
- L26: Triggers
- L36: Calls (outbound)
- L42: Called By (inbound)
- L50: Modes
- L52: Init Mode — `/rune docs init`
- L56: Update Mode — `/rune docs update`
- L60: API Mode — `/rune docs api`
- L64: Changelog Mode — `/rune docs changelog`
- L68: Executable Steps
- L70: Init Mode
- L86: [Project Name]
- L89: Quick Start
- L92: Features
- L95: Tech Stack
- L98: Project Structure
- L101: Configuration
- L104: Development
- L107: API Reference
- L110: License
- L118: Architecture
- L120: Overview
- L125: Key Decisions
- L128: Module Map
- L131: Data Flow
- L153: Update Mode
- L209: API Mode
- L237: API Reference
- L239: Authentication
- L242: Endpoints
- L244: `POST /api/auth/login`
- L267: Changelog Mode
- L284: Output Format
- L286: Init Mode Output
- L292: Update Mode Output
- L302: API Mode Output
- L305: `METHOD /path/:param`
- L313: Changelog Mode Output
- L316: Constraints
- L325: Returns
- L337: Sharp Edges
- L350: Done When
- L352: Init Mode
- L359: Update Mode
- L365: API Mode
- L371: Changelog Mode
- L376: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
