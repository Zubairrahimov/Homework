from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User

# Create your views here.


class UserGetView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteUpdateGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserGetAllView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserGetByIdView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


