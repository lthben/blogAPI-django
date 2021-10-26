from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .serializers import CommentSerializer
from .models import Post
from .models import Comment
from rest_framework import permissions

    # path('comment-list/<str:pk>/', views.CommentList.as_view(), name='comments-list'),
    # path('comment-create/', views.CommentCreate.as_view(), name='comment-create'),
    # path('post-update/<str:pk>/', views.CommentUpdate.as_view(), name='comment-update'),
    # path('post-delete/<str:pk>/', views.CommentDelete.as_view(), name='comment-delete'),

# Show all posts
class PostList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request):
        # posts = Post.objects.filter(user=request.user)
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

# Create (require JWT token)
class PostCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response('ok', status=201)

        else:
            return Response('Error with creating post', status=400)

# Update (require JWT token)
class PostUpdate(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data)

        if serializer.is_valid():
            # serializer.save(user=request.user)
            serializer.save() #no auth
        return Response('post updated')

# Delete (require JWT token)
class PostDelete(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def delete(self, request, pk):
        post = Post.objects.get(id=pk)
        post.delete()
        comments = Comment.objects.filter(post_id=pk)
        comments.delete()

        return Response('post deleted')

# Show all comments for one blog post
class CommentList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, pk):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

# Create (require JWT token)
class CommentCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            # post = Post.objects.get(id=pk)
            # serializer.validated_data['post_id'] = post.id
            # print(serializer.validated_data)
            serializer.save()

            return Response('ok', status=201)

        else:
            return Response('Error with creating comment', status=400)

# Update (require JWT token)
class CommentUpdate(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, pk):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(instance=comment, data=request.data)

        if serializer.is_valid():
            # serializer.save(user=request.user)
            serializer.save() #no auth

            return Response('comment updated', status=200)
        else:
            return Response('error updating comment', status=400)

# Delete (require JWT token)
class CommentDelete(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def delete(self, request, pk):
        comment = Comment.objects.get(id=pk)
        comment.delete()

        return Response('comment deleted')
