# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L16: onboard
- L18: Purpose
- L22: Triggers
- L28: Calls (outbound)
- L34: Called By (inbound)
- L40: Output Files
- L56: Executable Steps
- L58: Step 1 — Full Scan
- L70: Step 2 — Detect Tech Stack
- L89: Step 3 — Extract Conventions
- L100: Step 4 — Generate CLAUDE.md
- L105: Step 5 — Initialize .rune/ Directory
- L120: Step 5.4 — Detect Invariants (Auto-Discipline Seed)
- L147: Step 5.5 — Load Existing Instincts
- L159: Step 6b — Generate DEVELOPER-GUIDE.md
- L166: Developer Guide: [Project Name]
- L168: What This Does
- L171: Quick Setup
- L174: [Python projects] Activate virtual environment
- L177: Install dependencies
- L180: Run development server
- L183: Run tests
- L187: Key Files
- L191: How to Contribute
- L196: Common Issues
- L204: Who to Ask
- L210: Step 6c — Suggest L4 Extension Packs
- L236: Suggested L4 Packs
- L243: Step 6d — Context Budget Check
- L252: Context Budget Advisory
- L261: Step 6e — AI-Driven Interview (Optional, User-Initiated)
- L311: Step 6f — Emit comprehension.json
- L354: Step 7 — Commit
- L364: CLAUDE.md Template
- L367: [Project Name] — Project Configuration
- L369: Overview
- L372: Tech Stack
- L381: Directory Structure
- L384: Conventions
- L391: Commands
- L398: Key Files
- L404: Output Format
- L407: Onboard Report
- L411: Generated
- L419: Skipped (already exist)
- L422: Learned Instincts (if any)
- L426: Observations
- L431: Suggested L4 Packs
- L435: Constraints
- L444: Sharp Edges
- L455: Done When
- L464: Returns
- L475: Cost Profile

## Bundled files

- `upstream/references/invariants-template.md`
- `upstream/scripts/detect-invariants.js`
- `upstream/scripts/inject-claude-md.js`
- `upstream/scripts/onboard-invariants.js`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
