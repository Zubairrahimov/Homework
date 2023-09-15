from rest_framework import serializers
from .models import User10


class User10Serializer(serializers.ModelSerializer):
    class Meta:
        model = User10
        fields = '__all__'