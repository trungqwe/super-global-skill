# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: audit
- L19: Purpose
- L23: Triggers
- L30: Calls (outbound)
- L45: Called By (inbound)
- L51: Executable Instructions
- L53: Phase 0: Project Discovery
- L67: Phase 0.5: Context-Building (Pure Understanding)
- L85: Phase 1: Dependency Audit
- L97: Phase 2: Security Audit
- L110: Phase 3: Code Quality Audit
- L117: console.log in production code
- L120: TypeScript any types
- L123: Empty catch blocks
- L126: Python print() in production
- L129: Rust .unwrap() outside tests
- L155: Phase 4: Architecture Audit
- L215: Phase 5: Performance Audit
- L260: Phase 6: Infrastructure & DevOps Audit
- L294: Phase 7: Documentation Audit
- L312: Framework-Specific Checks
- L356: Phase 8: Mesh Analytics (H3 Intelligence)
- L381: Mesh Analytics
- L403: DX Review Mode (Addy Osmani 8 Principles)
- L412: DX Principle 1: Time to Hello World
- L432: DX Principle 2: First-Time Setup Friction
- L445: DX Principle 3: Error Message Quality
- L460: DX Principle 4: CLI Help Quality
- L476: DX Principle 5: Documentation Navigation
- L488: DX Principle 6: API Consistency
- L499: DX Principle 7: Progressive Disclosure
- L506: DX Principle 8: Recovery from Mistakes
- L513: DX Review Output
- L516: DX Review: [Project Name]
- L530: Quick Wins (fix in <1 hour)
- L535: Structural Improvements (plan needed)
- L543: Final Report
- L551: Weighted Composite Scoring
- L555: Scoring Formula
- L565: Grade Thresholds
- L575: Why Weighted (not average)
- L580: Severity Levels
- L592: Output Format
- L595: Audit Report: [Project Name]
- L602: Health Score
- L615: Phase Breakdown
- L627: Composite Score
- L631: Top Priority Actions
- L634: Positive Findings
- L637: Follow-up Timeline
- L645: Constraints
- L655: Mesh Gates
- L664: Returns
- L674: Sharp Edges
- L683: Done When
- L692: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
