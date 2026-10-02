# autonomous-project-ops

1. Establish acceptance criteria, relevant code paths and a short plan; reuse existing task state. Inspect only files needed for the next decision.
2. Make routine reversible decisions and complete authorized work. Ask only for missing input that materially changes behavior or authorization that is actually absent.
3. Implement a complete vertical slice and preserve unrelated changes. Use a regression check for behavioral defects; scale tests and process to risk.
4. When stuck, create a representative failing signal and test one cause at a time. Change strategy when evidence disproves the current approach.
5. Verify with actual project commands, current outputs, exit codes and nonempty target counts. Review the diff and user-visible behavior; update canonical docs when behavior changes.
6. Finish with outcome, evidence and material limitations. Do not claim a deployment from a local build or keep retesting without a new reason.
