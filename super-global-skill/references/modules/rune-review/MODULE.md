# rune-review

1. Read the diff in caller context; prioritize behavioral regressions, security boundaries, data integrity and test gaps.
2. Return only supported findings with severity, file/line and a concrete failure scenario. Verify a suspected issue before recommending a fix; state coverage limits.

Use current session tools and repository conventions. Scale checks to risk; do not recursively load other skills or assume permission from this file.

For domain-specific detail beyond these steps, inspect [references/index.md](references/index.md) and read only the relevant source section.
