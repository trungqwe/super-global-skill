# Hỗ trợ nền tảng

Bộ cài cài cùng một `super-global-skill` vào thư mục discovery global của nền tảng được chọn.

| Agent | Skill global mặc định | Native adapter |
|---|---|---|
| Codex | `~/.agents/skills` | Không cần plugin riêng |
| Claude Code | `~/.claude/skills` | Rules tùy chọn |
| OpenCode | `~/.config/opencode/skills`; cũng đọc `.agents`/`.claude` | Permission do người dùng cấu hình |
| Antigravity IDE | `~/.gemini/config/skills` | `~/.gemini/config/plugins` và rules |
| Antigravity CLI | `~/.gemini/antigravity-cli/skills` | `~/.gemini/antigravity-cli/plugins` và rules |
| Gemini CLI | `~/.gemini/skills` hoặc alias `.agents/skills` | `~/.gemini/GEMINI.md` tùy chọn |
| Cursor | `~/.cursor/skills` hoặc `~/.agents/skills` | Không cần plugin riêng |
| GitHub Copilot | `~/.copilot/skills` hoặc `~/.agents/skills` | Không cần plugin riêng |
| Windsurf/Devin | `~/.codeium/windsurf/skills` hoặc `~/.agents/skills` | Không cần plugin riêng |
| Cline | `~/.cline/skills` | Không cần plugin riêng |
| Generic | `~/.agents/skills` | Dùng `--skills-dir` cho layout khác |

Các đường dẫn được đối chiếu với tài liệu nền tảng ngày 03/10/2026. Không suy đoán quyền, model, connector, MCP hoặc khả năng native của phiên cụ thể; agent có thể yêu cầu restart/refresh.
