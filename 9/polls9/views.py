from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import User9Serializer
from .models import User9
# Create your views here.


class UserGetView(generics.ListCreateAPIView):
    queryset = User9.objects.all()
    serializer_class = User9Serializer

class UserDeleteUpdateGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User9.objects.all()
    serializer_class = User9Serializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User9.objects.all()
    serializer_class = User9Serializer

class UserCreateView(generics.CreateAPIView):
    queryset = User9.objects.all()
    serializer_class = User9Serializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User9.objects.all()
    serializer_class = User9Serializer

class UserGetAllView(generics.ListAPIView):
    queryset = User9.objects.all()
    serializer_class = User9Serializer

class UserGetByIdView(generics.RetrieveAPIView):
    queryset = User9.objects.all()
    serializer_class = User9Serializer


