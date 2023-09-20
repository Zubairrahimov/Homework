from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import NewsSerializer4
from .models import NewsModel4
from rest_framework.response import Response
# Create your views here.




class CreateAPiView4(APIView):
    def post(self, request, *args, **kwargs):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 2:
                serializer = NewsSerializer4(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            else:
                return Response({'msg': 'only staff members can add'})
        else:
            return Response({'msg': 'only staff members can add'})


class ListAPiView4(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user) == 'AnonymousUser':
            return Response({'msg': 'Please log in'})
        all = NewsModel4.objects.filter(status=True)
        serializer = NewsSerializer4(all, many=True)
        return Response(serializer.data)


class UpdateStatus4(APIView):
    def patch(self, request, *args, **kwargs):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 3:

                news = get_object_or_404(NewsModel4, id=kwargs['news_id'])
                serializer = NewsSerializer4(news, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
            else:
                return Response({'msg': 'only admins change status'})

        return Response({'msg': 'only admins change status'})


