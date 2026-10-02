# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: adversary
- L19: Purpose
- L31: Triggers
- L37: Calls (outbound)
- L48: Called By (inbound)
- L57: Cross-Hub Connections
- L66: Execution
- L68: Step 0: Load Context
- L75: Step 0.5: Steelman + Pick a Reasoning Lens
- L100: Step 0.6: Decorrelated Multi-Perspective Gathering (council, CRITICAL-tier only)
- L129: Step 1: Edge Case Analysis
- L149: Step 2: Security Attack Vectors
- L171: Step 3: Scalability Stress Test
- L193: Step 4: Error Propagation Analysis
- L213: Step 5: Integration Risk Assessment
- L233: Step 6: Verdict and Report
- L257: Output Format
- L260: Adversary Report: [feature/plan name]
- L268: CRITICAL
- L273: HIGH
- L278: MEDIUM
- L281: Strength Notes
- L284: Verdict
- L288: Workflow Modes
- L290: Full Red-Team (default)
- L293: Quick Challenge (for smaller plans)
- L297: Security-Focused
- L301: Mode: oracle (v0.2.0)
- L328: File 1: <relative/path/to/file.ts>
- L331: File 2: <...>
- L349: Constraints
- L362: Mesh Gates
- L369: Sharp Edges
- L390: Done When
- L402: Returns
- L412: Cost Profile

## Bundled files

- `upstream/evals.md`
- `upstream/references/context-bundle-format.md`
- `upstream/references/cross-model-escalation.md`
- `upstream/references/oracle-mode.md`
- `upstream/references/reasoning-modes.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
