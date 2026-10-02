# Nguồn và giới hạn

Đóng gói từ 79 entry point đã tối ưu, giữ các module và tài liệu Rune có điều kiện. Commit nguồn ở [upstream-lock.json](upstream-lock.json); các giấy phép gốc được giữ trong `licenses/`. Hash các entry nguồn được ghi trong `module-index.json` để xác định snapshot, không kèm đường dẫn cá nhân.

Gói này không sao chép skill hệ thống hay plugin thương mại của Codex, không kèm tài khoản, memory, config, AGENTS cá nhân hoặc runtime MemoryOS/Pinokio. Các kỹ thuật tích hợp từ Superpowers, AI Context Master và Agent Skills Standard đã được điều chỉnh theo workflow portable.

Các module Pinokio dựa trên bản workflow cục bộ đã tối ưu; chưa xác định được upstream công khai chính xác. Các đường dẫn máy nguồn được thay bằng biến mô tả cần resolve trên máy nhận. Những tham chiếu này không chứng minh API runtime mới nhất.

SHA-256 của package dùng để phát hiện sai lệch nội dung, không phải chữ ký số xác thực nhà phát hành.
