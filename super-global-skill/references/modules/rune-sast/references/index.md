# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: sast
- L17: Purpose
- L23: Triggers
- L30: Calls (outbound)
- L34: Called By (inbound)
- L41: Execution
- L43: Step 1 — Detect Language and Tools
- L63: Step 2 — Run Primary Analysis
- L78: ESLint (JS/TS) — security-focused rules
- L81: Bandit (Python) — security scanner
- L84: Semgrep (any language) — pattern-based analysis
- L87: Clippy (Rust) — lint + security
- L90: govulncheck (Go) — vulnerability check
- L94: Step 3 — Run Semgrep (If Available)
- L107: Step 4 — Normalize to Unified Format
- L131: Step 5 — Report
- L134: SAST Report
- L141: BLOCK (must fix)
- L145: WARN (should fix)
- L148: INFO
- L151: Tool Coverage
- L159: Output Format
- L163: Constraints
- L172: Sharp Edges
- L182: Done When
- L190: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
