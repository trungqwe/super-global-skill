# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: fix
- L19: Purpose
- L28: Triggers
- L36: Calls (outbound)
- L48: Called By (inbound)
- L58: Cross-Hub Connections
- L65: Execution
- L67: Step 1: Understand
- L76: Step 1b: Recovery Policy Matrix
- L99: Step 2: Locate
- L108: Step 3: Change
- L119: Step 4: Verify
- L130: Step 4.5: Quality Decay Check (Self-Regulation)
- L156: Step 5: Post-Fix Hardening (Defense-in-Depth)
- L171: Step 5b: Preserve Debug Instrumentation
- L182: Step 6: Self-Review
- L190: Step 6b: Capture Fix Pattern
- L194: Step 7: Report
- L202: Constraints
- L213: Scope Gate
- L225: Mesh Gates
- L232: Output Format
- L235: Fix Report
- L239: Changes
- L243: Verification
- L248: Concerns (if DONE_WITH_CONCERNS)
- L251: Context Needed (if NEEDS_CONTEXT)
- L254: Blocker (if BLOCKED)
- L257: Notes
- L261: Status Protocol (Subagent Contract)
- L272: Returns
- L280: Chain Metadata
- L302: Sharp Edges
- L320: Done When
- L332: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
