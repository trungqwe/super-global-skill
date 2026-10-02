# Báo cáo audit và hợp nhất

## Nguồn đã kiểm tra

- `everything-everywhere-for-antigravity` tại commit `68a4398e3dd32c83831bc4720024ed95a91c6757` (6.874 file, 322 skill entry ở `skills/`, 12 plugin).
- `E:\Coding backup\skill-find-repo.zip`, SHA-256 `B4AADB208033BF5EE3F47708BB43BB16AD57649FEE16D29C75139DA005065B06` (bundle ReuseForge 1.0.0, 9 member ZIP, manifest báo 9/9 PASS).
- `E:\Coding backup\Codex\codex-super-global-skill.zip`, SHA-256 `6EDB59BAAA266E34345338E78CC8BA43A9A47BB5D4E50B7F98BB4DB52EBE8124` (bộ cài giao dịch an toàn, 79 module).

## Kết quả chắt lọc

- Giữ `super-global-skill` làm một entry point duy nhất để các agent hỗ trợ cùng một router.
- Hợp nhất 79 Codex core module, catalog Antigravity, plugin variant có khác biệt và 9 ReuseForge skill vào `references/skill-index.json`.
- Giữ nguyên payload Antigravity dưới `super-global-skill/references/platforms/antigravity/` để installer có thể nạp plugin/rules riêng cho IDE. Các bản skill trùng nội dung được dùng một bản canonical để tránh mơ hồ.
- ReuseForge được giải nén thành các reference skill riêng; outer ZIP không được coi là một skill duy nhất.
- Router hỗ trợ tiếng Việt có dấu, tiếng Anh, alias cụm từ và tối đa năm ứng viên; agent tự chọn skill theo ngữ cảnh thay vì buộc người dùng gọi tên.

## Findings và biện pháp

| Mức | Finding | Xử lý |
|---|---|---|
| Cao | Script cài Antigravity gốc sao chép đè trực tiếp vào thư mục người dùng, không có checksum/rollback | Không dùng làm installer mặc định; bộ cài mới có manifest, backup, rollback và từ chối ghi đè bản không quản lý |
| Cao | `elite-workflows-and-taste/skills/ship/sections/apple-release.md` có chỉ dẫn trì hoãn việc nói cho người dùng biết credential bền vững đã được tạo và lưu trên máy | Giữ nguyên file upstream để truy nguyên nhưng đánh dấu là reference rủi ro; entry point mới buộc bỏ qua chỉ dẫn che giấu credential, bỏ qua approval hoặc tự cấp authority. Dùng `--skip-plugins` nếu không cần plugin upstream |
| Trung bình | Antigravity có 284 bản skill trùng ở plugin và `skills/`, cùng 9 bản khác nội dung | Chọn `skills/` làm canonical; ghi lại 9 plugin variant với hậu tố `@antigravity-plugin`; giữ plugin payload cho native IDE |
| Trung bình | Nhiều skill chứa lệnh cài package, network/API và thao tác credential theo domain | Chỉ lưu làm reference; installer không thực thi; entry point yêu cầu kiểm tra tool, quyền và credential theo từng tác vụ |
| Thấp | ReuseForge outer bundle yêu cầu tải từng member ZIP | Đã giải nén và tích hợp 9 member, đồng thời giữ manifest/checksum nguồn để truy nguyên |
| Chưa xác minh | Native discovery trên mọi phiên bản Codex/Claude/OpenCode/Antigravity | Installer có dry-run/verify; tài liệu yêu cầu mở phiên mới hoặc refresh skill sau cài |

## Giới hạn

Static audit không thay thế sandbox runtime, signature verification của upstream, hay kiểm thử native trên mọi hệ điều hành. Không có API key, runtime, plugin registry hoặc quyền truy cập dịch vụ nào được cấp bởi gói này.
