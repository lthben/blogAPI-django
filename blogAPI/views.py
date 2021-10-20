from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
# from rest_framework import permissions


# path('post-list/', views.PostList.as_view(), name='post-list'),
# path('post-create/', views.PostCreate.as_view(), name='post-create'),
# path('post-update/<str:pk>/', views.PostUpdate.as_view(), name='post-update'),
# path('post-delete/<str:pk>/', views.PostDelete.as_view(), name='post-delete'),

# The APIs required (using JWT)
# Login
# Logout
# Refresh Token

# Show all posts
class PostList(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        # posts = Post.objects.filter(user=request.user)
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)


# Create (require JWT token)
class PostCreate(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            # serializer.save(user=request.user)
            serializer.save()

            return Response('ok', status=201)

        else:
            return Response('Error with creating', status=400)

# Update (require JWT token)
class PostUpdate(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data)

        if serializer.is_valid():
            # serializer.save(user=request.user)
            serializer.save()
        return Response('updated')


# Delete (require JWT token)
class PostDelete(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    def delete(self, request, pk):
        post = Post.objects.get(id=pk)
        post.delete()

        return Response('item deleted')
