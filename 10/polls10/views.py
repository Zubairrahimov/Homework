from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import User10Serializer
from .models import User10

# Create your views here.


class UserGetView(generics.ListCreateAPIView):
    queryset = User10.objects.all()
    serializer_class = User10Serializer

class UserDeleteUpdateGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User10.objects.all()
    serializer_class = User10Serializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User10.objects.all()
    serializer_class = User10Serializer

class UserCreateView(generics.CreateAPIView):
    queryset = User10.objects.all()
    serializer_class = User10Serializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User10.objects.all()
    serializer_class = User10Serializer

class UserGetAllView(generics.ListAPIView):
    queryset = User10.objects.all()
    serializer_class = User10Serializer

class UserGetByIdView(generics.RetrieveAPIView):
    queryset = User10.objects.all()
    serializer_class = User10Serializer


