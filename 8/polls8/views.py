from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import User8Serializer
from .models import User8

# Create your views here.


class UserGetView(generics.ListCreateAPIView):
    queryset = User8.objects.all()
    serializer_class = User8Serializer

class UserDeleteUpdateGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User8.objects.all()
    serializer_class = User8Serializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User8.objects.all()
    serializer_class = User8Serializer

class UserCreateView(generics.CreateAPIView):
    queryset = User8.objects.all()
    serializer_class = User8Serializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User8.objects.all()
    serializer_class = User8Serializer

class UserGetAllView(generics.ListAPIView):
    queryset = User8.objects.all()
    serializer_class = User8Serializer

class UserGetByIdView(generics.RetrieveAPIView):
    queryset = User8.objects.all()
    serializer_class = User8Serializer


