from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<str:folder>/', views.topic_detail, name='topic_detail'),
    path('topic/<str:folder>/file/<path:filename>', views.serve_topic_file, name='serve_topic_file'),
    
    # Auth URLs
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
