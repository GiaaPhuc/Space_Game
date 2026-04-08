# 🚀 Space Game (Python)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/library-Pygame-green.svg)](https://www.pygame.org/)

Một trò chơi bắn máy bay không gian cổ điển được xây dựng bằng ngôn ngữ **Python** và thư viện **Pygame**. Dự án tập trung vào việc áp dụng các nguyên lý lập trình hướng đối tượng (OOP) để quản lý thực thể và logic trong game một cách chuyên nghiệp.

---

## 🎮 Tính năng nổi bật

- **Hệ thống di chuyển:** Điều khiển mượt mà bằng bàn phím (WASD hoặc Phím mũi tên).
- **Cơ chế chiến đấu:** Hệ thống bắn đạn (Bullets) và xử lý va chạm (Collision Detection) thời gian thực.
- **Quản lý thực thể:** Tách biệt logic người chơi (Player) và kẻ địch (Enemy) giúp dễ dàng mở rộng.
- **Tùy biến linh hoạt:** Dễ dàng điều chỉnh thông số game (tốc độ, số lượng đạn, FPS) thông qua file cấu hình riêng.

---

## 📂 Cấu trúc thư mục

Dự án được tổ chức theo cấu trúc module hóa để dễ quản lý:

```text
.
├── assets/             # Chứa hình ảnh, âm thanh và tài nguyên game
│   └── ships/          # Các mẫu tàu vũ trụ và kẻ địch (Sprites)
├── bullet.py           # Xử lý logic đạn, di chuyển và biến mất khi ra khỏi màn hình
├── enemy.py            # Quản lý hành vi, vị trí xuất hiện của kẻ địch
├── player.py           # Logic điều khiển, máu và trạng thái người chơi
├── settings.py         # Cấu hình hằng số (FPS, kích thước màn hình, màu sắc)
├── main.py             # File thực thi chính (Vòng lặp Game Loop & Xử lý sự kiện)
└── README.md           # Hướng dẫn sử dụng và thông tin dự án
```

## 🛠️ Hướng dẫn cài đặt

### 1. Yêu cầu hệ thống

- Máy tính đã cài sẵn **Python 3.x**.
- Trình quản lý gói **pip**.

### 2. Cài đặt thư viện

Mở Terminal hoặc Command Prompt tại thư mục dự án và chạy lệnh:

```bash
pip install pygame
```

### 3. Khởi chạy Game

Chạy file chính để bắt đầu trò chơi:

```bash
python main.py
```

## ⌨️ Cách điều khiển

Người chơi có thể sử dụng linh hoạt các phím sau để điều hướng trong không gian:

| Hành động      | Phím điều khiển          |
| :------------- | :----------------------- |
| **Di chuyển**  | `←`, `→`                 |
| **Bắn đạn**    | `Phím Space` (Phím cách) |
| **Thoát game** | Nhấn dấu `X`             |
