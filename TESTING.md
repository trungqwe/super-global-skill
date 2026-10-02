# Kiểm thử gói

Chạy từ thư mục đã giải nén:

```powershell
python -B install.py --verify
python -B -m unittest discover -s tests -v
```

Test dùng thư mục tạm, kiểm tra checksum, định tuyến tiếng Việt/Anh, cài universal và native trong các profile, dry-run không ghi file, xung đột unmanaged bị chặn, replace tạo backup và rollback khôi phục cây cũ. Không test trực tiếp app native, plugin registry, runtime bên ngoài hoặc mọi hệ điều hành.
