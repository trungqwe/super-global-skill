# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: autopsy
- L17: Purpose
- L21: Called By (inbound)
- L28: Calls (outbound)
- L35: Execution Steps
- L37: Step 0 — Repo intelligence (if GitHub-hosted)
- L42: Fetch via GitHub API (requires gh CLI or curl + GITHUB_TOKEN)
- L45: Contributor count and top contributors
- L49: Commit frequency (last 52 weeks)
- L52: Language byte distribution
- L63: Step 1 — Structure scan
- L72: Step 2 — Module analysis
- L83: Step 3 — Health scoring
- L102: Step 4 — Risk assessment
- L107: Most changed files (hotspots)
- L110: Files not touched in over a year
- L113: Authors per file (high author count = high churn risk)
- L116: Commit velocity by month (trend detection)
- L119: Issue/PR close rate (GitHub only)
- L130: Step 5 — Generate RESCUE-REPORT.md
- L135: Rescue Report: [Project Name]
- L138: Overall Health: [score]/100
- L140: Module Health
- L145: Dependency Graph
- L148: Language Distribution
- L151: Commit Velocity (Last 12 Months)
- L154: Repo Intelligence (GitHub only)
- L163: Surgery Queue (Priority Order)
- L167: Git Archaeology
- L172: Immediate Actions (Before Surgery)
- L179: Step 5b — Emit comprehension.json
- L218: Step 6 — Report
- L228: Confidence Scoring
- L245: Multi-Round Analysis
- L256: Health Score Factors
- L267: Output Format
- L270: Autopsy Report: [Project Name]
- L272: Overall Health: [score]/100 — [tier: healthy | watch | at-risk | critical]
- L274: Module Summary
- L279: Top Issues
- L282: Next Step
- L286: Constraints
- L294: Sharp Edges
- L306: Done When
- L316: Returns
- L327: Cost Profile
- L333: Executive Mode (--executive)
- L337: Executive Execution Steps
- L357: Executive Output
- L365: Color Coding
- L374: Graceful Degradation
- L380: External Repo Mode (--external)
- L384: When to use --external
- L392: External Execution Steps
- L402: Core metadata
- L411: Maintainer responsiveness (issue + PR close rates)
- L418: Release cadence (last 10 releases)
- L421: Security advisories
- L424: Dependabot alerts (if accessible — usually not for external repos)
- L477: External Repo Evaluation: [owner/repo]
- L482: Quick Verdict
- L485: Decision Rubric (5 dimensions)
- L488: Activity Signal
- L493: Maintainership Signal
- L499: Adoption Signal
- L504: License
- L508: Security
- L513: Architecture (extracted, not read)
- L519: Confidence
- L522: Recommendation
- L526: External Mode Constraints
- L535: Graceful Degradation (External Mode)
- L542: Hand-offs (External Mode)

## Bundled files

- `upstream/references/repo-analysis-patterns.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
