# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: skill-forge
- L17: Purpose
- L21: Triggers
- L27: Calls (outbound)
- L35: Called By (inbound)
- L40: References
- L44: Workflow
- L46: Phase 1 — DISCOVER
- L60: Phase 2 — RED (Baseline Test)
- L67: Pressure Scenario: [skill-name]
- L69: Setup
- L72: Pressures (combine 2-3)
- L79: Expected Failure (without skill)
- L82: Success Criteria (with skill)
- L96: Phase 3 — GREEN (Write Minimal Skill)
- L170: BAD: Summarizes workflow — agent reads description, skips full content
- L173: GOOD: Only triggers — agent must read full content to know workflow
- L184: BAD: Generic rule
- L187: GOOD: Blocks specific failure with consequence
- L201: Phase 4 — VERIFY (Green Check)
- L215: Phase 5 — REFACTOR (Close Loopholes)
- L282: Phase 5.25 — SCRIPT CONTRACT (skills with helper scripts only)
- L361: Contract smoke test:
- L389: Phase 5.5 — SECURITY MODEL
- L396: Security Model
- L398: Trust Boundaries
- L403: This Skill Will NEVER
- L408: Threat Surface
- L430: Phase 6 — INTEGRATE
- L441: Phase 6.25 — EXAMPLES (output-format skills only)
- L481: Phase 6.5 — EXTENSION AUTHORING (if building an extension, not a skill)
- L544: Phase 7 — EVAL (Behavior Tests)
- L574: Phase 8 — SHIP
- L580: Add any updated existing skills
- L584: Skill Quality Checklist
- L625: Adapting Existing Skills
- L639: Token Efficiency Guidelines
- L656: Output Format
- L659: Skill Forge Report
- L664: Baseline Test
- L669: Quality Checklist
- L674: Files Created/Modified
- L679: Mesh Impact
- L686: Constraints
- L696: Sharp Edges
- L713: Done When
- L722: Returns
- L732: Cost Profile

## Bundled files

- `upstream/references/claude-skill-reference.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
