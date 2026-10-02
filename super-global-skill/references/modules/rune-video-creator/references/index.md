# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: video-creator
- L17: Purpose
- L21: Called By (inbound)
- L26: Calls (outbound)
- L30: Executable Instructions
- L32: Step 1: Receive Brief
- L47: Step 2: Script
- L70: Step 3: Storyboard
- L90: Step 4: Shot List
- L113: Step 5: Assets Needed
- L123: Step 6: Report
- L128: Video Plan: [topic]
- L135: Script
- L138: Storyboard
- L141: Shot List
- L144: Assets Needed
- L147: Platform Notes
- L154: Video Plan Created
- L162: Next Steps
- L168: Narration Craft (decides whether a script hooks or bores)
- L196: Voiceover: TTS-Safe Narration (when narration is machine-spoken)
- L233: Note
- L237: Output Format
- L241: Constraints
- L247: Sharp Edges
- L261: Done When
- L273: Cost Profile

## Bundled files

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
