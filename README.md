# Library Management System

Ứng dụng quản lý thư viện / sách đơn giản giao diện dòng lệnh (CLI) được viết bằng **Python** và cơ sở dữ liệu **MySQL**.

## 🚀 Tính năng
- ➕ **Thêm sách mới**: Nhập tên sách, tác giả, giá tiền và số lượng.
- ✏️ **Cập nhật thông tin sách**: Sửa thông tin theo ID (hỗ trợ nhấn Enter để giữ nguyên giá trị cũ).
- 🗑️ **Xóa sách**: Xóa sách khỏi hệ thống với xác nhận trước khi xóa.
- 🔍 **Tìm kiếm sách**: Tìm sách theo từ khóa tiêu đề.
- 📜 **Danh sách sách có sẵn**: Hiển thị bảng danh sách các sách hiện có trong kho bằng thư viện `tabulate`.

## 🛠️ Công nghệ sử dụng
- Python 3.x
- MySQL
- `mysql-connector-python`
- `tabulate`

## 📋 Hướng dẫn cài đặt

### 1. Yêu cầu hệ thống
- Python 3.8+
- Server MySQL đang chạy

### 2. Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt