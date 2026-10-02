# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: hallucination-guard
- L17: Purpose
- L21: Triggers
- L29: Calls (outbound)
- L31: Exception: L3→L3 coordination
- L34: Called By (inbound)
- L46: Execution
- L48: Step 1 — Extract imports
- L62: Step 2 — Verify internal imports
- L81: Step 3 — Verify external packages (Dependency Check Before Import)
- L108: Step 3.5 — Slopsquatting Registry Verification
- L147: Step 4 — Verify API calls
- L155: Step 5 — Report
- L159: Check Types
- L169: Output Format
- L172: Hallucination Guard Report
- L177: BLOCK (hallucination detected)
- L181: WARN (verify manually)
- L184: SUSPICIOUS (potential slopsquatting)
- L187: Verified
- L191: Constraints
- L198: Sharp Edges
- L212: Done When
- L221: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
