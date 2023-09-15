from rest_framework import serializers
from .models import User8

class User8Serializer(serializers.ModelSerializer):
    class Meta:
        model = User8
        fields = '__all__'

        