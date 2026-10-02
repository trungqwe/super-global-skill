# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L17: test
- L48: Instructions
- L50: Phase 1: Understand What to Test
- L71: Phase 2: Detect Test Framework
- L89: Phase 3: Write Failing Tests
- L133: Phase 3.5: Cycle Discipline (Vertical Slicing Gate)
- L161: Phase 4: Run Tests — Verify They FAIL (RED)
- L176: Phase 5: After Implementation — Verify Tests PASS (GREEN)
- L188: Phase 6: Coverage Check
- L195: Phase 6.5: Diff-Aware Mode (optional)
- L212: Test Types — 4-Layer Methodology
- L238: TEST.md — Test Plan + Results Document
- L242: Before writing tests — write the plan:
- L244: Test Plan: [Feature Name]
- L246: Test Inventory
- L251: Unit Test Plan (L1)
- L256: E2E Scenarios (L3/L4)
- L261: Realistic Workflow Scenarios
- L265: After tests pass — append results:
- L267: Test Results
- L270: Summary
- L274: Requirement Coverage
- L280: Gaps
- L286: Skill Behavior Tests (Eval Scenarios)
- L290: Eval Scenario Format
- L293: Eval: E[NN] — [scenario name]
- L295: Prompt
- L298: Expected Reasoning
- L301: Must Include
- L305: Must NOT
- L309: Category
- L313: Eval Coverage Requirements
- L326: Eval Storage
- L331: Error Recovery
- L338: Called By (inbound)
- L356: Calls (outbound)
- L362: Data Flow
- L364: Feeds Into →
- L370: Fed By ←
- L376: Feedback Loops ↻
- L381: Anti-Rationalization Table
- L395: Advanced: Oracle-Injection E2E Testing
- L417: Spec→Test Traceability
- L443: Eval-Driven Development
- L447: Two Eval Types
- L458: Eval File Format
- L463: Eval: <feature name>
- L465: Capability Evals (pass@k)
- L470: Regression Evals (pass^k)
- L476: Anti-Pattern: Eval Overfitting
- L483: Integration with TDD
- L491: Red Flags — STOP and Start Over
- L504: Constraints
- L519: Mesh Gates
- L527: Output Format
- L530: Test Report
- L536: Test Cases
- L541: Coverage
- L545: Regressions (if any)
- L549: Testing Anti-Patterns (Gate Functions)
- L553: Anti-Pattern 1: Testing Mock Behavior
- L557: Anti-Pattern 2: Test-Only Methods in Production
- L561: Anti-Pattern 3: Mocking Without Understanding Side Effects
- L565: Anti-Pattern 4: Incomplete Mocks
- L569: Anti-Pattern 5: Mock Setup Longer Than Test Logic
- L573: Anti-Pattern 6: Test Slop (Framework-Behavior Tests)
- L591: Returns
- L601: Chain Metadata
- L628: Sharp Edges
- L648: Self-Validation
- L660: Done When
- L672: Cost Profile

## Bundled files

- `upstream/evals.md`
- `upstream/references/mocking-policy.md`
- `upstream/references/test-quality.md`
- `upstream/references/vertical-tdd.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
