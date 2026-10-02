# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: ba
- L18: Purpose
- L34: Triggers
- L41: Calls (outbound)
- L49: Called By (inbound)
- L58: Cross-Hub Connections
- L65: Executable Steps
- L67: Step 1 — Intake & Classify
- L84: Step 1.4 — Synthesis Trigger Check
- L103: Step 1.5 — Out-of-Scope Match Check (READ)
- L129: Step 1.6 — Mid-Elicitation Reject WRITE Path
- L173: Step 2.0 — Explore-First Pre-Check (HARD-GATE)
- L199: Step 2 — Requirement Elicitation (the "5 Questions")
- L258: Step 2.5 — Ambiguity Scoring (Execution Gate)
- L324: Step 2.6 — CONTEXT.md Cross-Reference Gate
- L341: Step 3 — Hidden Requirement Discovery
- L364: Step 3.5 — Completeness Scoring (Options & Alternatives)
- L389: Step 3.6 — Logic Consistency Check
- L438: Step 4 — Scope Definition
- L454: Step 4.5 — Functional Requirements (EARS)
- L484: Step 5 — User Stories & Acceptance Criteria
- L506: Step 5.5 — Key Entities (mandatory if feature involves data)
- L511: Key Entities
- L522: Step 6 — Non-Functional Requirements (NFRs)
- L536: Step 6.5 — Tiered Recommendations
- L551: Quick Win (0-30 days)
- L557: Differentiation (1-3 months)
- L563: Long-term Moat (6-12 months)
- L577: Step 7 — Artifact Triad
- L592: Requirements Document: [Feature Name]
- L595: Context
- L598: Stakeholders
- L602: User Stories
- L605: Functional Requirements
- L608: Key Entities
- L611: Scope
- L612: In Scope
- L613: Out of Scope
- L614: Assumptions
- L616: Non-Functional Requirements
- L619: Dependencies
- L622: Risks
- L625: Strategic Recommendations
- L628: Logic Consistency Report
- L631: Next Step
- L673: Implementation Tasks: [Feature Name]
- L675: Foundational (blocking prerequisites)
- L680: US-1 [P1]: [story title]
- L690: US-2 [P2]: [story title]
- L693: NFR Verification
- L711: Step 7.5 — Glossary Sharpen (CONTEXT.md update)
- L728: Output Format
- L746: Constraints
- L763: Returns
- L773: Sharp Edges
- L821: Done When
- L840: Cost Profile

## Bundled files

- `upstream/references/context-md-format.md`
- `upstream/references/ears-format.md`
- `upstream/references/explore-first.md`
- `upstream/references/out-of-scope-format.md`
- `upstream/references/synthesis-mode.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
