from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
import os

TOPICS = [
    {'num': '01', 'icon': '🔢', 'title': 'Hệ số và Chuyển đổi cơ số', 'folder': '01_He_so_va_Chuyen_doi_co_so'},
    {'num': '02', 'icon': '📐', 'title': 'Tiền tố và Trung tố', 'folder': '02_Tien_to_va_Trung_to'},
    {'num': '03', 'icon': '🔄', 'title': 'Đệ quy', 'folder': '03_De_quy'},
    {'num': '04', 'icon': '💾', 'title': 'Thao tác chuỗi Bit', 'folder': '04_Thao_tac_chuoi_bit'},
    {'num': '05', 'icon': '🌿', 'title': 'LISP', 'folder': '05_LISP'},
    {'num': '06', 'icon': '🧩', 'title': 'What Does This Program Do?', 'folder': '06_ACSL_What_Does_This_Program_Do'},
    {'num': '07', 'icon': '📚', 'title': 'Tài liệu PDF', 'folder': '07_Tai_lieu_PDF'},
    {'num': '08', 'icon': '⚡', 'title': 'Boolean Algebra', 'folder': '08_Boolean_Algebra'},
    {'num': '09', 'icon': '🔄', 'title': 'FSA & Regular Expressions', 'folder': '09_FSA_Regular_Expressions'},
    {'num': '10', 'icon': '🔗', 'title': 'Graph Theory', 'folder': '10_Graph_Theory'},
    {'num': '11', 'icon': '🔌', 'title': 'Digital Electronics', 'folder': '11_Digital_Electronics'},
    {'num': '12', 'icon': '💻', 'title': 'Assembly Language', 'folder': '12_Assembly_Language'},
]

def index(request):
    """Main portal page showing all ACSL topics."""
    return render(request, 'index.html', {'topics': TOPICS})

def topic_detail(request, folder):
    """List files in a topic folder."""
    # Find topic info
    topic = next((t for t in TOPICS if t['folder'] == folder), None)
    if not topic:
        raise Http404("Topic not found")
    
    # Get files from folder
    folder_path = settings.TOPICS_DIR / folder
    if not folder_path.exists():
        raise Http404("Folder not found")
    
    files = []
    for f in sorted(folder_path.iterdir()):
        if f.is_file() and not f.name.startswith('.'):
            files.append({
                'name': f.name,
                'ext': f.suffix.lower(),
                'url': f'/topic/{folder}/file/{f.name}'
            })
    
    return render(request, 'topic_detail.html', {'topic': topic, 'files': files})

def serve_topic_file(request, folder, filename):
    """Serve a file from a topic folder."""
    file_path = settings.TOPICS_DIR / folder / filename
    if not file_path.exists() or not file_path.is_file():
        raise Http404("File not found")
    
    # Determine content type
    ext = file_path.suffix.lower()
    content_types = {
        '.html': 'text/html',
        '.pdf': 'application/pdf',
        '.py': 'text/plain',
        '.js': 'application/javascript',
        '.css': 'text/css',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.gif': 'image/gif',
    }
    content_type = content_types.get(ext, 'application/octet-stream')
    
    return FileResponse(open(file_path, 'rb'), content_type=content_type)

