from django.urls import path
from . import views

urlpatterns = [
    path('blog-list/', views.BlogList.as_view(), name='blog-list'),
    path('blog-create/', views.BlogCreate.as_view(), name='blog-create'),
    path('blog-update/<str:pk>/', views.BlogUpdate.as_view(), name='blog-update'),
    path('blog-delete/<str:pk>/', views.BlogDelete.as_view(), name='blog-delete'),
]
