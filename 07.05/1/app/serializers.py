from rest_framework import serializers
from .models import Shoxrux


class ShoxruxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoxrux
        fields = ('sana', 'dars1')


