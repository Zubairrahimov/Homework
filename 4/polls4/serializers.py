from rest_framework.serializers import ModelSerializer

from . models import NewsModel4
class NewsSerializer4(ModelSerializer):
    class Meta:
        model = NewsModel4
        fields = ('__all__')