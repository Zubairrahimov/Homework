from django.shortcuts import render , get_object_or_404
from .models import Shoxrux
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShoxruxSerializer


# Create your views here.

class ListedVersion(APIView):
    def get(self, request):
        all_data = Shoxrux.objects.all()
        seria = ShoxruxSerializer(all_data , many= True)
        return Response(seria.data)
    
class InDetail(APIView):
    def get(self, request, *args, **kwargs):
        savol = get_object_or_404(Shoxrux, id=kwargs['savol_id'])
        seria2 = ShoxruxSerializer(savol)
        return Response(seria2.data)

class Alish(APIView):
    def post(self, request):
        seria3 = request.data
        alisa = ShoxruxSerializer(data = seria3)
        if alisa.is_valid:
            alisa.save()
            return Response(alisa.data)
        return Response({alisa.errors})


class UpadateQuestionView(APIView):
    def patch(self, request, *args, **kwargs):
        question = get_object_or_404(Shoxrux, id = kwargs['savol_id'])
        serializer = ShoxruxSerializer(question , data=request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class DeleteQuestionView(APIView):
    def delete(self, request, *args, **kwargs):
        question = get_object_or_404(Shoxrux,  id = kwargs['savol_id'])
        question.delete()
        return Response({'message': 'Question deleted sir'})
    
