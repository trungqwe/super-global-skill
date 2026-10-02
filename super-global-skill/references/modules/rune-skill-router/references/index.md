# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: Live Routing Context
- L22: skill-router
- L24: Purpose
- L30: Triggers
- L36: Calls (outbound connections)
- L40: Called By (inbound connections)
- L44: Workflow
- L46: Step 0 — Check Routing Overrides (H3 Adaptive Routing)
- L69: Context Efficiency (Trigger-Table Pattern)
- L78: Step 0.25 — Request Classifier (Fast-Path Filter)
- L96: Step 0.3 — Skill Discovery (`/rune list`)
- L105: Rune Skills Catalog
- L107: Core Skills (L0-L3) — Always Available
- L112: Extension Packs (L4) — Domain Knowledge
- L117: Pro/Business Packs (if installed)
- L127: Step 0.5 — STOP before responding
- L137: Step 1 — Intent Classification (Progressive Disclosure)
- L248: Step 1.5 — File Ownership Matrix (Constraint Inheritance)
- L268: Step 2 — Compound Intent Resolution
- L290: Step 3 — Anti-Rationalization Gate
- L305: Step 4 — Execute
- L313: Step 5 — Post-Completion Neural Memory Capture
- L326: Routing Exceptions
- L334: Proactive Skill Recommendations (One-Hop Max)
- L338: Chain Metadata Awareness (Priority Source)
- L359: Hardcoded Fallback Table
- L400: Output Format
- L402: Routing Proof (Required in Every Code Response)
- L412: Full Routing Decision (when announcing route)
- L415: Routing Decision
- L426: Routing Chain
- L432: Constraints
- L442: Sharp Edges
- L452: Done When
- L458: Self-Verification Trigger (MANDATORY)
- L476: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
