# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: session-bridge
- L19: Purpose
- L23: Triggers
- L33: Calls (outbound)
- L35: Exception: L3→L3 coordination (same pattern as hallucination-guard → research)
- L38: Called By (inbound)
- L48: State Files Managed
- L62: Execution
- L64: Save Mode (end of session or pre-compaction)
- L89: [YYYY-MM-DD HH:MM] Decision: <title>
- L104: [YYYY-MM-DD] Convention: <title>
- L113: [YYYY-MM-DD] Convention: Async-First I/O
- L127: [YYYY-MM-DD HH:MM] Session Summary
- L165: Task Notes: [task name]
- L166: What Worked (with evidence)
- L169: What Failed
- L172: What's Left
- L175: Key Context for Next Iteration
- L190: [YYYY-MM-DD] Instinct: <short name>
- L262: Cumulative Project Notes
- L264: Project Profile
- L269: Architecture Map
- L274: Recurring Themes
- L279: Active Topics
- L284: Relationship Map
- L289: Follow-Up Items
- L293: Attention Points
- L337: Load Mode (start of session)
- L440: Checkpoint Mode (explicit save-and-resume point)
- L451: Checkpoint — [YYYY-MM-DD HH:MM]
- L453: What I Was Doing
- L456: Current Git State
- L462: Decisions Made This Session (Load-Bearing)
- L467: What's Left (Ordered)
- L472: Context the Next Session Needs
- L477: Resume Command
- L488: Checkpoint Saved
- L515: Output Format
- L517: Save Mode
- L519: Session Bridge — Saved
- L527: Load Mode
- L529: Session Bridge — Loaded
- L539: Checkpoint Mode
- L541: Checkpoint Saved
- L547: Detach Mode (v0.8.0)
- L553: Step D1 — Receive dispatch
- L562: Step D2 — Idempotency check
- L566: Step D3 — Write pending record
- L587: Step D4 — Return control to caller
- L591: Step D5 — Reattach (called by primary agent between phases)
- L601: Step D6 — Cleanup
- L605: Pending Record Schema
- L620: Constraints
- L628: Sharp Edges
- L646: Done When (Save Mode)
- L656: Done When (Load Mode)
- L666: Done When (Checkpoint Mode)
- L675: Done When (Detach Mode)
- L683: Cost Profile

## Bundled files

- `upstream/references/detach-protocol.md`
- `upstream/references/evolutionary-memory-patterns.md`
- `upstream/scripts/load-invariants.js`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
