from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import NewsSerializer3
from .models import NewsModel3
from rest_framework.response import Response
# Create your views here.




class CreateAPiView3(APIView):
    def post(self, request, *args, **kwargs):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 2:
                serializer = NewsSerializer3(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            else:
                return Response({'msg': 'only staff members can add'})
        else:
            return Response({'msg': 'only staff members can add'})


class ListAPiView3(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user) == 'AnonymousUser':
            return Response({'msg': 'Please log in'})
        all = NewsModel3.objects.filter(status=True)
        serializer = NewsSerializer3(all, many=True)
        return Response(serializer.data)


class UpdateStatus3(APIView):
    def patch(self, request, *args, **kwargs):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 3:

                news = get_object_or_404(NewsModel3, id=kwargs['news_id'])
                serializer = NewsSerializer3(news, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            else:
                return Response({'msg': 'only admins change status'})

        return Response({'msg': 'only admins change status'})


