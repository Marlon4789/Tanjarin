
from django.urls import path, include
from . import views

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.home, name='home'),
    path('show_posts/', views.show_posts, name='show_posts'),
    path('detail/<int:quillpost_id>/', views.quillpost_detail, name='detail'),
    path('form_blocks/', include('form_blocks.urls')),
] 
