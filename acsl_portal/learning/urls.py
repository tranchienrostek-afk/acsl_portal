from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<str:folder>/', views.topic_detail, name='topic_detail'),
    path('topic/<str:folder>/file/<path:filename>', views.serve_topic_file, name='serve_topic_file'),
]

