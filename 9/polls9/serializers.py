from rest_framework import serializers
from .models import User9

class User9Serializer(serializers.ModelSerializer):
    class Meta:
        model = User9
        fields = '__all__'

        