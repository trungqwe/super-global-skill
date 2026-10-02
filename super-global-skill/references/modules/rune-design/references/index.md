# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: design
- L17: Purpose
- L21: Triggers
- L28: Calls (outbound)
- L35: Called By (inbound)
- L45: Output Files
- L52: Executable Steps
- L54: Step 0 — Load Design Reference
- L69: External Data Source
- L80: Step 1 — Discover
- L90: Step 2 — Classify Product Domain
- L109: Step 2.5 — Mood-to-Constraint Mapping
- L134: Step 2.7 — Tweaks, Not Menus (Default Style Pattern)
- L150: Step 2.9 — Universal Anti-AI Rules (apply to ALL domains)
- L195: Unwired Elements
- L259: Step 3 — Apply Domain Reasoning Rules
- L381: Step 4 — Platform-Specific Overrides
- L422: Step 5 — Generate Design System File
- L427: Design System: [Project Name]
- L433: Color Tokens
- L435: Primitive (raw values)
- L438: Semantic (meaning-mapped)
- L450: Typography
- L462: Spacing (8px base)
- L465: Border Radius
- L468: Effects
- L471: Anti-Patterns (MUST NOT generate these)
- L476: Platform Notes
- L479: Component Library
- L482: Pre-Delivery Checklist
- L501: Step 5.4 — Render Blindness (advisory)
- L526: Step 5.5 — UI Design Contract (UI-SPEC.md)
- L535: UI Specification: [Project Name]
- L538: Layout Decisions
- L544: Visual Hierarchy Rules
- L550: Component Decisions
- L556: Locked Anti-Decisions (things we explicitly chose NOT to do)
- L564: Step 6 — Accessibility Review
- L580: Step 6.5 — 6-Pillar Visual Audit
- L596: Visual Audit Score: [total]/24
- L613: Step 7 — UX Writing Patterns
- L636: Step 8 — Report
- L641: Design Report: [Project Name]
- L643: Domain Classification
- L646: Design System Generated
- L649: Key Decisions
- L654: Anti-Patterns Registered (will be flagged by review)
- L658: Pre-Delivery Checklist
- L662: Output Format
- L665: Design Report: TradingOS Dashboard
- L667: Domain Classification
- L670: Design System Generated
- L673: Key Decisions
- L681: Anti-Patterns Registered
- L685: Pre-Delivery Checklist
- L689: Constraints
- L706: Mesh Gates (L1/L2 only)
- L722: Returns
- L733: Sharp Edges
- L758: Done When
- L776: Cost Profile

## Bundled files

- `upstream/DESIGN-REFERENCE.md`
- `upstream/MOTION-CRAFT.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
