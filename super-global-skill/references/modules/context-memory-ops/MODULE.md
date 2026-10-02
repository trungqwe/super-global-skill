# context-memory-ops

1. Find the repository canonical checkpoint and restore only the current objective, explicit constraints and relevant decisions. Verify dates and current file state.
2. Write one compact checkpoint: objective; completed work; decisions and reasons; changed paths; verification commands/results; blocker; next action.
3. Link to detailed logs and artifacts instead of copying them. Replace stale state; distinguish observation, inference and pending work.
4. Persist at meaningful milestones or before compaction, not on every tool call. Keep secrets and unrelated personal data out of memory.
5. Use local files by default. Use AI Context Master or remote memory only when that runtime is requested and available; do not bootstrap external infrastructure for an ordinary handoff.
