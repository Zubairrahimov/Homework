from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import NewsSerializer
from .models import NewsModel1
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import StaffPermissionClass , AdminPermissionClass

# Create your views here.


class CreateNewsAPIView(generics.CreateAPIView):
    queryset = NewsModel1.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, StaffPermissionClass)


class ListNewsAPIView(generics.ListAPIView):
    queryset = NewsModel1.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)

    

# class CreateAPiView(APIView):
#     def post(self, request, *args, **kwargs):
#         if str(request.user) != 'AnonymousUser':
#             if request.user.roles == 2:
#                 serializer = NewsSerializer(data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#             else:
#                 return Response({'msg': 'only staff members can add'})
#         else:
#             return Response({'msg': 'only staff members can add'})


# class ListAPiView(APIView):
#     def get(self, request, *args, **kwargs):
#         if str(request.user) == 'AnonymousUser':
#             return Response({'msg': 'Please log in'})
#         all = NewsModel1.objects.filter(status=True)
#         serializer = NewsSerializer(all, many=True)
#         return Response(serializer.data)


# class UpdateStatus(APIView):
#     def patch(self, request, *args, **kwargs):
#         if str(request.user) != 'AnonymousUser':
#             if request.user.roles == 3:

#                 news = get_object_or_404(NewsModel1, id=kwargs['news_id'])
#                 serializer = NewsSerializer(news, data=request.data, partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#             else:
#                 return Response({'msg': 'only admins change status'})

#         return Response({'msg': 'only admins change status'})


class UpdateStatusNewsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsModel1.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, AdminPermissionClass)