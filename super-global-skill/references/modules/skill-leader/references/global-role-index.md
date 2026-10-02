# Overlap resolution

- skill-leader selects skills; it does not run another mandatory orchestration pipeline.
- autonomous-project-ops owns delivery; workflow-orchestrator owns a durable staged plan when needed.
- context-memory-ops owns checkpoints; Rune journal/session/context wrappers and AI Context Master are opt-in compatibility routes.
- Specialist security, review and testing checks are selected by risk, not by counting files.
- System and plugin format specialists own their native artifacts; rune-doc-processor only selects the appropriate workflow.

Prefer explicit user choice, then repository-local fit, then the smallest adequate global workflow. Do not merge duplicate skill names across discovery roots.
