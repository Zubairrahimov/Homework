from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import User3Serializer
from .models import User3

# Create your views here.


class UserGetView(generics.ListCreateAPIView):
    queryset = User3.objects.all()
    serializer_class = User3Serializer

class UserDeleteUpdateGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User3.objects.all()
    serializer_class = User3Serializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User3.objects.all()
    serializer_class = User3Serializer

class UserCreateView(generics.CreateAPIView):
    queryset = User3.objects.all()
    serializer_class = User3Serializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User3.objects.all()
    serializer_class = User3Serializer

class UserGetAllView(generics.ListAPIView):
    queryset = User3.objects.all()
    serializer_class = User3Serializer

class UserGetByIdView(generics.RetrieveAPIView):
    queryset = User3.objects.all()
    serializer_class = User3Serializer


