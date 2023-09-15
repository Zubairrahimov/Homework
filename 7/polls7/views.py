from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import User7Serializer
from .models import User7

# Create your views here.


class UserGetView(generics.ListCreateAPIView):
    queryset = User7.objects.all()
    serializer_class = User7Serializer

class UserDeleteUpdateGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User7.objects.all()
    serializer_class = User7Serializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User7.objects.all()
    serializer_class = User7Serializer

class UserCreateView(generics.CreateAPIView):
    queryset = User7.objects.all()
    serializer_class = User7Serializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User7.objects.all()
    serializer_class = User7Serializer

class UserGetAllView(generics.ListAPIView):
    queryset = User7.objects.all()
    serializer_class = User7Serializer

class UserGetByIdView(generics.RetrieveAPIView):
    queryset = User7.objects.all()
    serializer_class = User7Serializer


