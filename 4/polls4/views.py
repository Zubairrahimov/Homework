from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import User4Serializer
from .models import User4

# Create your views here.


class UserGetView(generics.ListCreateAPIView):
    queryset = User4.objects.all()
    serializer_class = User4Serializer

class UserDeleteUpdateGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User4.objects.all()
    serializer_class = User4Serializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User4.objects.all()
    serializer_class = User4Serializer

class UserCreateView(generics.CreateAPIView):
    queryset = User4.objects.all()
    serializer_class = User4Serializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User4.objects.all()
    serializer_class = User4Serializer

class UserGetAllView(generics.ListAPIView):
    queryset = User4.objects.all()
    serializer_class = User4Serializer

class UserGetByIdView(generics.RetrieveAPIView):
    queryset = User4.objects.all()
    serializer_class = User4Serializer


