from rest_framework.serializers import ModelSerializer

from . models import NewsModel5
class NewsSerializer5(ModelSerializer):
    class Meta:
        model = NewsModel5
        fields = ('__all__')