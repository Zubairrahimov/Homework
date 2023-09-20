from rest_framework.serializers import ModelSerializer

from . models import NewsModel2
class NewsSerializer2(ModelSerializer):
    class Meta:
        model = NewsModel2
        fields = ('__all__')