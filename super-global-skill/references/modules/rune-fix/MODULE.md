# rune-fix

1. Read the failing behavior, caller contract and surrounding tests; establish the expected result before editing.
2. Fix at the responsible seam, preserve unrelated work and verify the regression plus affected callers. If the cause is unclear, investigate before adding another patch.

Use current session tools and repository conventions. Scale checks to risk; do not recursively load other skills or assume permission from this file.

For domain-specific detail beyond these steps, inspect [references/index.md](references/index.md) and read only the relevant source section.
