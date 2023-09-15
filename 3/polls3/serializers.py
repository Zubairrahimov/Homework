from rest_framework import serializers
from .models import User3

class User3Serializer(serializers.ModelSerializer):
    class Meta:
        model = User3
        fields = '__all__'
        