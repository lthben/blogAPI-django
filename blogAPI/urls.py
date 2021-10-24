from django.urls import path
from . import views

urlpatterns = [
    path('post-list/', views.PostList.as_view(), name='post-list'),
    path('post-create/', views.PostCreate.as_view(), name='post-create'),
    path('post-update/<str:pk>/', views.PostUpdate.as_view(), name='post-update'),
    path('post-delete/<str:pk>/', views.PostDelete.as_view(), name='post-delete'),
    path('comment-list/<str:pk>/', views.CommentList.as_view(), name='comments-list'),
    path('comment-create/', views.CommentCreate.as_view(), name='comment-create'),
    path('comment-update/<str:pk>/', views.CommentUpdate.as_view(), name='comment-update'),
    path('comment-delete/<str:pk>/', views.CommentDelete.as_view(), name='comment-delete'),
]
