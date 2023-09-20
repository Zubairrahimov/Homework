from rest_framework.serializers import ModelSerializer

from . models import NewsModel1
class NewsSerializer(ModelSerializer):
    class Meta:
        model = NewsModel1
        fields = ('__all__')