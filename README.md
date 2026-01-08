# ACSL Learning Portal

Cổng học tập ACSL Việt Nam - Django web portal cho tài liệu ACSL.

## 🚀 Quick Start

### Development (Local)

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
cd acsl_portal
python manage.py runserver
```

Truy cập: http://localhost:8000

### Production (Docker)

```bash
# Build and run
docker-compose up -d --build

# View logs
docker-compose logs -f
```

Truy cập: http://localhost:8000

## 📁 Cấu trúc

```
├── acsl_portal/          # Django project
│   ├── learning/         # Main app
│   └── static/           # Static files
├── 01-12_*/              # Topic folders (12 ACSL topics)
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🌐 Triển khai toàn quốc

1. **VPS/Cloud**: Deploy Docker container lên AWS, GCP, Azure
2. **Domain**: Trỏ domain về server IP
3. **SSL**: Sử dụng Let's Encrypt cho HTTPS
4. **CDN**: Sử dụng Cloudflare để tối ưu tốc độ

## 📚 12 Chủ đề ACSL

1. Hệ số và Chuyển đổi cơ số
2. Tiền tố và Trung tố
3. Đệ quy
4. Thao tác chuỗi Bit
5. LISP
6. What Does This Program Do?
7. Tài liệu PDF
8. Boolean Algebra
9. FSA & Regular Expressions
10. Graph Theory
11. Digital Electronics
12. Assembly Language
