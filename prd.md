# PRD - ACSL Learning Portal

## 1. Tổng quan dự án
ACSL Learning Portal là một nền tảng học tập trực tuyến tập trung vào các nội dung của kỳ thi American Computer Science League (ACSL). Mục tiêu của dự án là cung cấp một kho lưu trữ tài liệu, bài tập và mô phỏng tương tác tập trung, giúp học sinh Việt Nam dễ dàng tiếp cận và ôn luyện cho kỳ thi.

## 2. Mục tiêu dự án
*   **Hệ thống hóa:** Sắp xếp 12 chủ đề chính của ACSL một cách khoa học.
*   **Tiếp cận dễ dàng:** Cung cấp giao diện hiện đại, thân thiện và hỗ trợ thiết bị di động.
- **Tính tương tác:** Tích hợp các công cụ mô phỏng để minh họa các khái niệm trừu tượng (Boolean, FSA, Lisp...).
- **Triển khai diện rộng:** Sử dụng Docker để có thể triển khai nhanh chóng trên các nền tảng cloud (Render, AWS, v.v.).

## 3. Đối tượng người dùng
*   **Học sinh:** Những người đang ôn thi ACSL muốn tìm kiếm tài liệu và làm bài tập.
*   **Giáo viên/Huấn luyện viên:** Sử dụng portal như một công cụ giảng dạy và quản lý tài liệu.

## 4. Các tính năng chính (v1.0)
### 4.1. Trang chủ (Portal Index)
- Cửa sổ tìm kiếm chủ đề nhanh.
- Danh sách 12 thẻ chủ đề (Topic Cards) với icon và số thứ tự.
- Thống kê tổng quan (Số chủ đề, tài liệu, câu hỏi).

### 4.2. Quản lý tài liệu (Topic Detail)
- Tự động liệt kê các file trong thư mục của từng chủ đề.
- Hỗ trợ xem trực tiếp các định dạng file: `.html`, `.pdf`, `.py`.
- Bảo mật: Yêu cầu đăng nhập để truy cập tài liệu.

### 4.3. Hệ thống tài khoản (Auth)
- Đăng ký tài khoản học sinh mới.
- Đăng nhập/Đăng xuất bảo mật.
- Redirect thông minh về trang đang xem sau khi đăng nhập.

### 4.4. Cơ sở hạ tầng
- **Dockerized:** Chạy mượt mà trên mọi môi trường với Docker Compose.
- **Cloud Ready:** Cấu hình sẵn cho Render.com (PostgreSQL/SQLite).

## 5. Công nghệ sử dụng
*   **Backend:** Django (Python 3.11+)
*   **Frontend:** HTML5, Vanilla CSS3 (Modern dark theme), JavaScript.
*   **Serving:** Gunicorn, Whitenoise (Static files).
*   **DevOps:** Docker, Docker Compose, Git.

## 6. Lộ trình phát triển (Roadmap)
- [ ] **Giai đoạn 2:** Tích hợp hệ thống làm bài tập trắc nghiệm có chấm điểm tự động.
- [ ] **Giai đoạn 3:** Dashboard theo dõi tiến độ học tập của từng học sinh.
- [ ] **Giai đoạn 4:** Diễn đàn thảo luận dưới mỗi bài học.
