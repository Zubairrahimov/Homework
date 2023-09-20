from rest_framework.serializers import ModelSerializer

from . models import NewsModel3
class NewsSerializer3(ModelSerializer):
    class Meta:
        model = NewsModel3
        fields = ('__all__')