# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L18: deploy
- L20: Purpose
- L30: Called By (inbound)
- L35: Calls (outbound)
- L48: Cross-Hub Connections
- L53: Execution Steps
- L55: Step 1 — Pre-deploy checks (HARD-GATE)
- L73: Step 1.5 — Release Checklist (Production Deploys Only)
- L92: Rollback Plan: v<version>
- L94: Trigger Conditions
- L97: Steps
- L103: Verification
- L108: Post-Rollback
- L116: Step 2 — Detect platform
- L137: Step 3 — Deploy
- L151: Step 4 — Verify deployment
- L163: Step 4.5 — Post-Deploy Health Thresholds
- L181: Step 5 — Monitor
- L185: Step 6 — Report
- L190: Deploy Report
- L196: Checks
- L206: Progressive Rollout / Feature Flag Mode
- L210: Progressive Rollout Chain
- L227: Feature Flag Integration
- L244: Skip if
- L249: Managed vs Self-Host Crossover
- L277: Verify cost allocation tags exist on managed resources
- L278: AWS: aws resourcegroupstaggingapi get-resources --tag-filters Key=Environment
- L279: GCP: gcloud asset search-all-resources --query='labels:environment'
- L280: Vercel: project settings → check team/project tagging
- L281: If untagged → BLOCK with COST_UNATTRIBUTED finding
- L284: Observability Cost in Deploys
- L297: Instrumentation Readiness (pre-prod advisory gate)
- L315: Output Format
- L319: Constraints
- L329: Returns
- L339: Sharp Edges
- L356: Done When
- L365: Cost Profile

## Bundled files

- `upstream/references/observability.md`
- `upstream/references/post-deploy-integration.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
