# Super Global Skill — bắt đầu nhanh

Đây là một skill portable có entry point `super-global-skill`, router tự chọn skill từ yêu cầu tiếng Việt/Anh và payload native cho nhiều agent.

## Cài đặt nhanh

```powershell
python install.py --verify
python install.py --agent codex
```

Chọn `claude`, `opencode`, `antigravity`, `antigravity-cli`, `gemini`, `cursor`, `copilot`, `windsurf`, `cline`, `generic` hoặc `all`. Dùng `--dry-run` để xem kế hoạch; `--install-rules` để cài rules; `--skip-plugins` để bỏ plugin Antigravity; `--universal-only` để chỉ cài entry point.

```powershell
python install.py --agent antigravity --install-rules
python install.py --agent all --dry-run
```

Bộ cài có checksum, staging, backup và rollback. Nếu đích đã có bản không do bộ cài quản lý, lệnh dừng; chỉ dùng `--replace` sau khi đã review.

## Tự động chọn workflow

Agent đọc `super-global-skill/SKILL.md` trước. Khi yêu cầu không khớp hiển nhiên, dùng:

```powershell
python super-global-skill/scripts/route.py "soi lỗi API và review PR"
```

Router chỉ tra cứu tối đa năm ứng viên, không tải mạng và không thực thi skill. Agent đọc một workflow chính và nhiều nhất hai workflow hỗ trợ.

## Phạm vi

Gói giữ 79 core module Codex, 322 skill và plugin Antigravity, cùng 9 ReuseForge skill đã kiểm tra checksum. Native discovery còn phụ thuộc phiên bản agent và cần restart/refresh sau cài. Gói không cấp tool, connector, runtime, model, tài khoản hay credential.

Xem `AUDIT.md`, `README-VI.md` và `super-global-skill/references/provenance.json` để biết finding, nguồn và giới hạn kiểm chứng.
