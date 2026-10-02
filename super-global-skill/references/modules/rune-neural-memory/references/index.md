# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L33: neural-memory
- L35: Purpose
- L41: Triggers
- L58: Calls (outbound)
- L62: Called By (inbound)
- L77: Modes
- L79: Mode 1: Recall (Session Start / Before Decisions)
- L113: Mode 2: Capture (After Task Completion)
- L169: Mode 3: Hypothesis Tracking
- L205: Mode 4: Flush (Session End / Pre-Compaction)
- L226: Mode 5: Maintenance (Weekly / On-Demand)
- L261: Output Format
- L263: Recall Report
- L265: Neural Memory Recall — <project>
- L267: Loaded Context
- L272: Applicable to Current Task
- L276: Gaps Detected
- L280: Capture Report
- L282: Neural Memory Capture — <task summary>
- L284: Saved Memories
- L291: Reinforced Topics
- L295: Health Report
- L297: Neural Memory Health
- L307: Recommended Actions
- L311: Constraints
- L321: Sharp Edges
- L332: Done When
- L355: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
