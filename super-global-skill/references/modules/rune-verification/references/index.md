# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: verification
- L21: Instructions
- L23: Phase 1: Detect Project Type
- L46: Phase 2: Run Lint
- L60: Phase 3: Run Type Check
- L71: Phase 4: Run Tests
- L86: Phase 5: Run Build
- L101: Phase 6: Generate Report
- L105: 3-Level Artifact Verification
- L174: Artifact Output Verification
- L211: Surface-Constraint Verification (the Constraint Loop)
- L252: Error Recovery
- L258: Calls (outbound)
- L262: Called By (inbound)
- L282: Output Format
- L292: 3-Level File Verification
- L302: Failures (if any)
- L313: Output Completion Enforcement
- L340: Evidence-Before-Claims Gate
- L348: Claim Validation Protocol
- L358: Red Flags — Agent is Lying
- L371: Constraints
- L381: Sharp Edges
- L402: Done When
- L412: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
