# Chỉ mục mô-đun

Đây là 79 tài liệu bên trong một skill. Tên cũ là alias; không gọi công cụ skill để tải chúng. Chọn một mô-đun chính và tối đa hai mô-đun hỗ trợ, đọc file bằng công cụ hiện có. Không đọc toàn bộ chỉ mục JSON hoặc tài liệu upstream.

## Điều phối, yêu cầu, kiến trúc

- [skill-leader](modules/skill-leader/MODULE.md): Use when a task spans multiple disciplines and needs skill selection.
- [autonomous-project-ops](modules/autonomous-project-ops/MODULE.md): Use when implementing or fixing a project end to end with verification.
- [workflow-orchestrator](modules/workflow-orchestrator/MODULE.md): Use when planning dependent stages, risks and durable progress for complex work.
- [architecture-solution-review](modules/architecture-solution-review/MODULE.md): Use when choosing architecture or technology with consequential tradeoffs.
- [rune-plan](modules/rune-plan/MODULE.md): Use when turning a complex requirement into an executable implementation plan.
- [rune-ba](modules/rune-ba/MODULE.md): Use when clarifying ambiguous product requirements or acceptance criteria.
- [rune-brainstorm](modules/rune-brainstorm/MODULE.md): Use when exploring materially different solutions to an open problem.
- [rune-adversary](modules/rune-adversary/MODULE.md): Use when stress-testing a proposed implementation before coding.
- [rune-problem-solver](modules/rune-problem-solver/MODULE.md): Use when structuring a complex problem with uncertain causes or tradeoffs.
- [rune-sequential-thinking](modules/rune-sequential-thinking/MODULE.md): Use when reasoning through an interdependent technical decision.

## Tìm mã, sửa lỗi, kiểm chứng

- [rune-scout](modules/rune-scout/MODULE.md): Use when locating code structure and implementation seams.
- [rune-fix](modules/rune-fix/MODULE.md): Use when applying a diagnosed bug fix or bounded implementation change.
- [rune-debug](modules/rune-debug/MODULE.md): Use when diagnosing reproducible or intermittent software failures.
- [rune-test](modules/rune-test/MODULE.md): Use when adding meaningful automated regression or behavior tests.
- [rune-verification](modules/rune-verification/MODULE.md): Use when verifying an implemented change with runnable checks.
- [rune-completion-gate](modules/rune-completion-gate/MODULE.md): Use when checking whether a completion claim is supported by evidence.
- [rune-hallucination-guard](modules/rune-hallucination-guard/MODULE.md): Use when verifying unfamiliar package names, imports or API calls.
- [rune-sentinel-env](modules/rune-sentinel-env/MODULE.md): Use when diagnosing a runtime, dependency or build-environment mismatch.

## Review, audit, bảo mật

- [rune-review](modules/rune-review/MODULE.md): Use when reviewing a code diff for actionable correctness issues.
- [rune-review-intake](modules/rune-review-intake/MODULE.md): Use when evaluating external code review feedback before implementation.
- [rune-audit](modules/rune-audit/MODULE.md): Use when auditing project health across security, architecture and quality.
- [rune-preflight](modules/rune-preflight/MODULE.md): Use when reviewing a change before committing or handing it off.
- [rune-sast](modules/rune-sast/MODULE.md): Use when running static security or quality analyzers.
- [rune-sentinel](modules/rune-sentinel/MODULE.md): Use when checking a change for exploitable security defects.
- [rune-integrity-check](modules/rune-integrity-check/MODULE.md): Use when checking imported instructions, persisted memory or agent artifacts for tampering.
- [rune-constraint-check](modules/rune-constraint-check/MODULE.md): Use when checking compliance with applicable task and repository requirements.
- [rune-scope-guard](modules/rune-scope-guard/MODULE.md): Use when checking whether changes remain within the requested scope.
- [rune-logic-guardian](modules/rune-logic-guardian/MODULE.md): Use when protecting complex business rules during edits.
- [rune-dependency-doctor](modules/rune-dependency-doctor/MODULE.md): Use when updating dependencies or investigating dependency vulnerabilities.
- [rune-perf](modules/rune-perf/MODULE.md): Use when investigating latency, resource usage or performance regressions.

## Refactor, Git, phát hành

- [rune-autopsy](modules/rune-autopsy/MODULE.md): Use when assessing a legacy codebase before a rescue or modernization.
- [rune-rescue](modules/rune-rescue/MODULE.md): Use when modernizing a legacy system incrementally.
- [rune-surgeon](modules/rune-surgeon/MODULE.md): Use when refactoring one bounded module while preserving behavior.
- [rune-safeguard](modules/rune-safeguard/MODULE.md): Use when establishing safety checks before a risky refactor.
- [rune-git](modules/rune-git/MODULE.md): Use when creating commits, branches, pull requests or resolving Git conflicts.
- [rune-worktree](modules/rune-worktree/MODULE.md): Use when creating an isolated Git checkout for concurrent or risky work.
- [rune-deploy](modules/rune-deploy/MODULE.md): Use when deploying an application to an explicitly selected environment.
- [rune-incident](modules/rune-incident/MODULE.md): Use when responding to a production outage or active service degradation.
- [rune-watchdog](modules/rune-watchdog/MODULE.md): Use when checking the health of a deployed release.
- [rune-scaffold](modules/rune-scaffold/MODULE.md): Use when bootstrapping a complete new software project.
- [rune-cook](modules/rune-cook/MODULE.md): Use when explicitly running a Rune implementation workflow.
- [rune-launch](modules/rune-launch/MODULE.md): Use when coordinating a release with explicitly requested launch materials.
- [rune-team](modules/rune-team/MODULE.md): Use when explicitly coordinating parallel agents on independent subtasks.

## Ngữ cảnh, tài liệu, nghiên cứu

- [context-memory-ops](modules/context-memory-ops/MODULE.md): Use when resuming, handing off or compacting an ongoing task.
- [rune-context-engine](modules/rune-context-engine/MODULE.md): Use when compacting a long task while preserving resumability.
- [rune-session-bridge](modules/rune-session-bridge/MODULE.md): Use when saving or restoring a cross-session project handoff.
- [rune-journal](modules/rune-journal/MODULE.md): Use when recording a durable architecture decision or project checkpoint.
- [ai-context-master](modules/ai-context-master/MODULE.md): Use when explicitly operating MemoryOS, Context Hub or the AI Context Master runtime.
- [rune-neural-memory](modules/rune-neural-memory/MODULE.md): Use when explicitly using a connected Neural Memory service.
- [rune-docs](modules/rune-docs/MODULE.md): Use when updating documentation to match a code or workflow change.
- [rune-onboard](modules/rune-onboard/MODULE.md): Use when creating concise project guidance for future agents.
- [rune-docs-seeker](modules/rune-docs-seeker/MODULE.md): Use when finding authoritative API documentation or resolving an error message.
- [rune-research](modules/rune-research/MODULE.md): Use when researching current external technical facts.
- [rune-trend-scout](modules/rune-trend-scout/MODULE.md): Use when researching current market or technology trends.
- [rune-skill-forge](modules/rune-skill-forge/MODULE.md): Use when creating or revising a reusable Rune skill.
- [rune-skill-router](modules/rune-skill-router/MODULE.md): Use when explicitly selecting a Rune specialist for a task.

## Giao diện, nội dung, công cụ

- [rune-design](modules/rune-design/MODULE.md): Use when defining a UI design system or interaction contract.
- [rune-browser-pilot](modules/rune-browser-pilot/MODULE.md): Use when reproducing or verifying browser UI behavior.
- [rune-asset-creator](modules/rune-asset-creator/MODULE.md): Use when creating SVG icons, social banners or code-based diagrams.
- [rune-doc-processor](modules/rune-doc-processor/MODULE.md): Use when choosing a workflow for PDF, Word, spreadsheet or slide artifacts.
- [rune-marketing](modules/rune-marketing/MODULE.md): Use when writing product positioning or launch content.
- [rune-video-creator](modules/rune-video-creator/MODULE.md): Use when planning a video script, storyboard or shot list.
- [rune-mcp-builder](modules/rune-mcp-builder/MODULE.md): Use when building or extending an MCP server.
- [pinokio](modules/pinokio/MODULE.md): Use when discovering, launching or inspecting apps through Pinokio.
- [gepeto](modules/gepeto/MODULE.md): Use when building or modifying Pinokio one-click launcher scripts.
- [rune-db](modules/rune-db/MODULE.md): Use when changing database schemas, queries or data migrations.

## Miền ứng dụng

- [rune-ext-ai-ml](modules/rune-ext-ai-ml/MODULE.md): Use when LLM, RAG, embeddings or ML integration.
- [rune-ext-analytics](modules/rune-ext-analytics/MODULE.md): Use when event tracking, experiments or product analytics.
- [rune-ext-backend](modules/rune-ext-backend/MODULE.md): Use when backend APIs, authentication, caching or background jobs.
- [rune-ext-chrome-ext](modules/rune-ext-chrome-ext/MODULE.md): Use when browser extension development.
- [rune-ext-content](modules/rune-ext-content/MODULE.md): Use when CMS, blog, MDX, localization or SEO systems.
- [rune-ext-devops](modules/rune-ext-devops/MODULE.md): Use when containers, CI/CD, infrastructure or service configuration.
- [rune-ext-ecommerce](modules/rune-ext-ecommerce/MODULE.md): Use when shopping carts, payments or commerce integrations.
- [rune-ext-gamedev](modules/rune-ext-gamedev/MODULE.md): Use when game loops, graphics, physics or interactive 3D.
- [rune-ext-mobile](modules/rune-ext-mobile/MODULE.md): Use when native or cross-platform mobile implementation.
- [rune-ext-saas](modules/rune-ext-saas/MODULE.md): Use when multi-tenant SaaS, subscriptions or feature entitlements.
- [rune-ext-security](modules/rune-ext-security/MODULE.md): Use when deep application security analysis.
- [rune-ext-trading](modules/rune-ext-trading/MODULE.md): Use when financial dashboards, market data or strategy research.
- [rune-ext-ui](modules/rune-ext-ui/MODULE.md): Use when frontend components, accessibility or responsive interaction.


## Universal catalog

`skill-index.json` contains the 79 Codex core modules, the Antigravity skill catalog, plugin variants, and the nine ReuseForge skills. `scripts/route.py` performs bounded Vietnamese/English lookup with diacritic normalization and phrase aliases. The full Antigravity payload is under `platforms/antigravity/`; its upstream `AGENTS.md` and `SOUL.md` are reference material and do not override host policy.
