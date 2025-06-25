import os
from pathlib import Path


# ข้อมูลระบบ
os_name = os.name
os_path = os.getcwd()
os_user = os.getenv("USERNAME")

print(os_user)

# ทำงานใน path
current_path = Path.cwd()


# สร้างโฟลเดอร์
make_foler = current_path /"test_123"
make_foler.mkdir(exist_ok=True)

# สร้างไฟล์
make_file = current_path / "test.txt"
# make_file.write_text("Hello, World!!!")

print(f"{make_file.stat().st_size} bytes")

# อ่านไฟล์
content_test = make_file
content = content_test.read_text(encoding="utf-8")
print(content)