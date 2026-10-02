# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: git
- L17: Purpose
- L21: Triggers
- L34: Calls (outbound)
- L38: Called By (inbound)
- L47: Modes
- L49: Commit Mode (default)
- L53: PR Mode
- L57: Branch Mode
- L61: Changelog Mode
- L65: Executable Steps
- L67: Commit Mode
- L116: PR Mode
- L127: Summary
- L130: Changes
- L133: Test Plan
- L136: Breaking Changes
- L146: Branch Mode
- L165: Changelog Mode
- L176: [Unreleased]
- L178: Added
- L181: Fixed
- L184: Changed
- L187: Removed
- L193: Release Mode
- L236: Output Format
- L238: Commit Mode
- L247: PR Mode
- L251: Summary
- L254: Changes
- L257: Test Plan
- L260: Breaking Changes
- L264: Branch Mode
- L270: Changelog Mode
- L272: [Unreleased]
- L274: Added
- L277: Fixed
- L280: Changed
- L284: Release Mode
- L286: Release: v<version>
- L294: Constraints
- L304: Sharp Edges
- L315: Done When
- L317: Commit Mode
- L324: PR Mode
- L330: Branch Mode
- L334: Changelog Mode
- L339: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
