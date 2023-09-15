from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import User5Serializer
from .models import User5

# Create your views here.


class UserGetView(generics.ListCreateAPIView):
    queryset = User5.objects.all()
    serializer_class = User5Serializer

class UserDeleteUpdateGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User5.objects.all()
    serializer_class = User5Serializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User5.objects.all()
    serializer_class = User5Serializer

class UserCreateView(generics.CreateAPIView):
    queryset = User5.objects.all()
    serializer_class = User5Serializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User5.objects.all()
    serializer_class = User5Serializer

class UserGetAllView(generics.ListAPIView):
    queryset = User5.objects.all()
    serializer_class = User5Serializer

class UserGetByIdView(generics.RetrieveAPIView):
    queryset = User5.objects.all()
    serializer_class = User5Serializer


