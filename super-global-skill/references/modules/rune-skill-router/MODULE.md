# Internal specialist routing

1. If project guidance names a matching local skill, honor it. Otherwise use this package's root routing table, then the matching section of `references/index.md` at the root of codex-super-global-skill.
2. Read the chosen `references/modules/<alias>/MODULE.md` directly. These are internal documents, not installed skills that require a vendor Skill tool.
3. Keep one primary module and at most two concrete support modules. Do not invoke an orchestrator to select another orchestrator, refresh a global registry, or bootstrap an upstream mesh.
4. Use `scripts/route.py` only for bounded keyword lookup when the right module is unclear. A missing result means inspect the relevant index section, not guess an unavailable tool.
