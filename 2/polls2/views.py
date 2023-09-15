from django.shortcuts import render
from rest_framework import generics
from .models import User2
from .serializers import User2Serializer

# Create your views here.


class UserGetView(generics.ListCreateAPIView):
    queryset = User2.objects.all()
    serializer_class = User2Serializer

class UserDeleteUpdateGetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User2.objects.all()
    serializer_class = User2Serializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User2.objects.all()
    serializer_class = User2Serializer

class UserCreateView(generics.CreateAPIView):
    queryset = User2.objects.all()
    serializer_class = User2Serializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset = User2.objects.all()
    serializer_class = User2Serializer

class UserGetAllView(generics.ListAPIView):
    queryset = User2.objects.all()
    serializer_class = User2Serializer

class UserGetByIdView(generics.RetrieveAPIView):
    queryset = User2.objects.all()
    serializer_class = User2Serializer


