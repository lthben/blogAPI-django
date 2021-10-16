from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import permissions


# path('blog-list/', views.BlogList.as_view(), name='blog-list'),
# path('blog-create/', views.BlogCreate.as_view(), name='blog-create'),
# path('blog-update/<str:pk>/', views.BlogUpdate.as_view(), name='blog-update'),
# path('blog-delete/<str:pk>/', views.BlogDelete.as_view(), name='blog-delete'),

# The APIs required (using JWT)
# Login
# Logout
# Refresh Token

# Show all blogs
class BlogList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)

        return Response(serializer.data)


# Create (require JWT token)
class BlogCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response('ok')

        else:
            return Response('Error with creating')


# Update (require JWT token)
class BlogUpdate(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, pk):
        blog = Blog.objects.get(id=pk)
        serializer = BlogSerializer(instance=blog, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response('updated')


# Delete (require JWT token)
class BlogDelete(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def delete(self, request, pk):
        blog = Blog.objects.get(id=pk)
        blog.delete()

        return Response('item deleted')
