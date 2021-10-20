from django.urls import path
from . import views

urlpatterns = [
    path('post-list/', views.PostList.as_view(), name='post-list'),
    path('post-create/', views.PostCreate.as_view(), name='post-create'),
    path('post-update/<str:pk>/', views.PostUpdate.as_view(), name='post-update'),
    path('post-delete/<str:pk>/', views.PostDelete.as_view(), name='post-delete'),
    # path('$/', views.posts, name='posts'),
    # path('$/', views.comments, name='comments'),
    # path('', views.index, name='index'),
    # path('post/', views.individual_post, name='individual_post')
]
