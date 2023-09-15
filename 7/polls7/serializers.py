from rest_framework import serializers
from .models import User7

class User7Serializer(serializers.ModelSerializer):
    class Meta:
        model = User7
        fields = '__all__'