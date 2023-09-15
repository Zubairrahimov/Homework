from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import User6Serializer
from .models import User6

# Create your views here.


class UserGetView(generics.ListCreateAPIView):
    queryset = User6.objects.all()
    serializer_class = User6Serializer

class UserDeleteUpdateGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User6.objects.all()
    serializer_class = User6Serializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User6.objects.all()
    serializer_class = User6Serializer

class UserCreateView(generics.CreateAPIView):
    queryset = User6.objects.all()
    serializer_class = User6Serializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User6.objects.all()
    serializer_class = User6Serializer

class UserGetAllView(generics.ListAPIView):
    queryset = User6.objects.all()
    serializer_class = User6Serializer

class UserGetByIdView(generics.RetrieveAPIView):
    queryset = User6.objects.all()
    serializer_class = User6Serializer


