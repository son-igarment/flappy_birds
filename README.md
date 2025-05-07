# Flappy Bird
## Dự án của Phạm Lê Ngọc Sơn

Đây là một trò chơi Flappy Bird được viết bằng Python sử dụng thư viện Pygame.

![screenshot](screenshot1.png)

## Mô tả dự án

Flappy Bird là một trò chơi đơn giản nhưng gây nghiện, trong đó người chơi điều khiển một chú chim bay qua các cột ống. Mục tiêu là bay qua càng nhiều ống càng tốt mà không va chạm vào chúng.

## Cấu trúc dự án

```
.
├── assets/            # Chứa tất cả tài nguyên đồ họa và âm thanh
├── src/               # Mã nguồn chính của game
│   ├── entities/      # Các thực thể trong game (chim, ống, nền, etc.)
│   ├── utils/         # Các tiện ích và hàm hỗ trợ
│   ├── flappy.py      # Lớp chính điều khiển trò chơi
│   └── __init__.py    
├── main.py            # Điểm khởi đầu của ứng dụng
├── pyproject.toml     # Cấu hình dự án Python
├── flappy.ico         # Icon của ứng dụng
├── Makefile           # Chứa các lệnh để chạy và quản lý dự án
└── README.md          # Tài liệu hướng dẫn (file này)
```

## Cách cài đặt

1. Đảm bảo bạn đã cài đặt Python 3.6 trở lên. Tải Python từ [python.org](https://www.python.org/downloads/)

2. Clone dự án này về máy của bạn:
   ```
   git clone <url_repository>
   cd flappy_birds
   ```

3. Cài đặt các thư viện cần thiết:
   ```
   make init
   ```
   (Hoặc chạy `pip install -r requirements.txt` nếu bạn không sử dụng make)

## Cách chơi

1. Chạy trò chơi bằng lệnh:
   ```
   make
   ```
   Hoặc:
   ```
   python main.py
   ```

2. Điều khiển:
   - Nhấn phím **Space** hoặc phím **↑** để làm chim bay lên
   - Nhấn phím **Esc** để thoát khỏi trò chơi

3. Chế độ gỡ lỗi (hiển thị hình chữ nhật và tọa độ):
   ```
   DEBUG=True make
   ```

4. Chạy trò chơi trên trình duyệt web (sử dụng pygbag):
   ```
   make web
   ```

## Tính năng

- Đồ họa đẹp mắt với hiệu ứng hoạt hình mượt mà
- Âm thanh sống động
- Hệ thống tính điểm
- Chế độ ngày/đêm thay đổi
- Đa nền tảng: chạy trên Windows, macOS, Linux và web

## Tác giả

Phạm Lê Ngọc Sơn

## Giấy phép

Dự án này được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## Lời cảm ơn

Cảm ơn cộng đồng pygame và nguồn cảm hứng từ trò chơi Flappy Bird gốc. 