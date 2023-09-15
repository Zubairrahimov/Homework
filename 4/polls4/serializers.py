from rest_framework import serializers
from .models import User4

class User4Serializer(serializers.ModelSerializer):
    class Meta:
        model = User4
        fields = '__all__'