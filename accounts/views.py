# accounts.views.py

# Here, we are adding all of the necessary imports for our LoginView
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer, TokenSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView

# JWT settings
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(generics.ListCreateAPIView):
    """
    POST user/login/
    """

    # This permission class will overide the global permission class setting
    # Permission checks are always run at the very start of the view, before any other code is allowed to proceed.
    # The permission class here is set to AllowAny, which overwrites the global class to allow anyone to have access to login.
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(data={
                # using DRF JWT utility functions to generate a token
                "token": str(refresh.access_token),
                })
            serializer.is_valid()
            return Response(serializer.data)
        else:
            return Response('Error logging in', status=400)

class RegisterUsersView(generics.ListCreateAPIView):
    """
    POST user/signup/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        first_name = request.data.get("first_name", "")
        last_name = request.data.get("last_name", "")
        if not username or not password or not email or not first_name or not last_name:
            return Response(
                data={
                    "message": "all fields are required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name
        )
        return Response(status=status.HTTP_201_CREATED)

class FirstNameView(APIView):
    """
    POST user/firstname/
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        user = User.objects.get(username=request.data["username"])
        serializer = UserSerializer(instance=user)
        return Response(serializer.data["first_name"])

