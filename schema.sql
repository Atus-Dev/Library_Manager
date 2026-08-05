-- 1. Tạo cơ sở dữ liệu (nếu chưa có) và chọn sử dụng
CREATE DATABASE IF NOT EXISTS library_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE library_db;

-- 2. Xóa bảng cũ nếu muốn làm sạch dữ liệu
DROP TABLE IF EXISTS books;

-- 3. Tạo bảng quản lý sách
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    quantity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 4. Thêm một số dữ liệu mẫu ban đầu để kiểm thử
INSERT INTO books (title, author, price, quantity) VALUES
('Lập Trình Python Cơ Bản', 'Nguyễn Văn A', 150000.00, 10),
('Cấu Trúc Dữ Liệu và Giải Thuật', 'Trần Thị B', 220000.00, 5),
('Nhập Môn Cơ Sở Dữ Liệu MySQL', 'Lê Văn C', 180000.00, 8),
('Clean Code - Mã Sạch', 'Robert C. Martin', 350000.00, 3);