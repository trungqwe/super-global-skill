# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: sentinel
- L19: Purpose
- L27: Triggers
- L36: Calls (outbound)
- L44: Called By (inbound)
- L56: Severity Levels
- L64: Security Patterns (built-in)
- L67: Secret patterns (regex)
- L73: OWASP patterns
- L79: Verification Route Selection
- L97: Executable Steps
- L99: Step 1 — Secret Scan (Gitleaks-Enhanced)
- L106: Step 2 — Dependency Audit
- L132: Step 3 — OWASP Check
- L138: Step 3.5 — Skill Content Security Guard
- L144: Step 4 — Destructive Command Guard
- L151: Step 4.5 — Framework-Specific Security Patterns
- L157: Step 4.6 — Config Protection (3-Layer Defense)
- L162: Step 4.7 — Fail-Open Detection
- L176: Step 4.8 — Agentic Security Scan
- L191: Step 4.85 — Contract Validation
- L207: Step 4.87 — Config Leak Threshold Detection
- L235: Step 4.86 — Organization Policy Enforcement (Business)
- L260: Organization Policy
- L269: Step 4.9 — Six-Gate Finding Validation
- L288: Step 5 — Report
- L305: WARN Acknowledgment Protocol
- L319: Step 5b — Domain Hook Generation (on request)
- L324: Output Format
- L327: Sentinel Report
- L333: BLOCK (must fix before commit)
- L343: WARN (must acknowledge)
- L350: INFO
- L356: Verdict
- L362: Constraints
- L374: Returns
- L384: Sharp Edges
- L399: Done When
- L410: Cost Profile

## Bundled files

- `upstream/references/auth-crypto-reference.md`
- `upstream/references/config-protection.md`
- `upstream/references/desktop-security.md`
- `upstream/references/destructive-commands.md`
- `upstream/references/domain-hooks.md`
- `upstream/references/framework-patterns.md`
- `upstream/references/owasp-patterns.md`
- `upstream/references/policy-driven-constraints.md`
- `upstream/references/secret-patterns.md`
- `upstream/references/skill-content-guard.md`
- `upstream/references/supply-chain.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
