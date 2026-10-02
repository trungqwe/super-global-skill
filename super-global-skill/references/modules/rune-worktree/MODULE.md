# rune-worktree

1. Inspect repository status and choose a worktree only when isolation is needed; honor the requested starting state.
2. Use the managed worktree tool when available, verify the returned path and preserve uncommitted work. Never recursively delete a computed path without checking its resolved boundary.

Use current session tools and repository conventions. Scale checks to risk; do not recursively load other skills or assume permission from this file.

For domain-specific detail beyond these steps, inspect [references/index.md](references/index.md) and read only the relevant source section.
