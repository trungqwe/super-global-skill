# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: problem-solver
- L17: Purpose
- L23: Calls (outbound)
- L27: Called By (inbound)
- L34: Execution
- L36: Input
- L45: Step 1 — Receive and Classify
- L59: Step 1.5 — Domain Classification (Cynefin)
- L75: Step 2 — Bias Check (ALWAYS RUN)
- L136: Step 3a — Select Analytical Framework
- L203: Step 3b — Decision Frameworks (when mode = "decide")
- L247: Step 3c — Decomposition Methods (when mode = "decompose")
- L264: Step 4 — Apply Framework
- L270: Step 5 — Apply Mental Models
- L289: Step 5.5 — Ethical Dimension Check (when applicable)
- L305: Step 6 — Generate Solutions
- L316: Step 6.5 — Decorrelated Judgment (council, high-stakes only)
- L331: Step 7 — Select Communication Structure
- L344: Constraints
- L357: Output Format
- L360: Analysis: [Problem Statement]
- L367: Bias Warnings
- L372: Reasoning Chain
- L378: Mental Model Cross-Check
- L381: Root Cause / Core Finding
- L384: Recommended Solutions (ranked)
- L393: Next Action
- L397: Sharp Edges
- L417: Done When
- L430: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
