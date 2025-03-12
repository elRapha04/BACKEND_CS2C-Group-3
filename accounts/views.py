from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User  = get_user_model()

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        # Authenticate the user
        user = authenticate(request, email=email, password=password)
        
        # Check if user is authenticated and email is verified
        if user is not None and user.is_active and user.is_verified:
            return Response({"message": "Login successful", "user": {"id": user.id, "email": user.email}}, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid credentials or email not verified"}, status=status.HTTP_400_BAD_REQUEST)