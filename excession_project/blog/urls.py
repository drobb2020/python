# Blog urls.py script

from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='Excession-blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='Excession-user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='Excession-post-detail'),
    path('post/new/', PostCreateView.as_view(), name='Excession-post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),
         name='Excession-post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),
         name='Excession-post-delete'),
    path('about/', views.about, name='Excession-blog-about'),
]
