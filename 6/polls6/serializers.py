from rest_framework import serializers
from .models import User6

class User6Serializer(serializers.ModelSerializer):
    class Meta:
        model = User6
        fields = '__all__'