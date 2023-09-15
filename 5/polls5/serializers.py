from rest_framework import serializers
from .models import User5

class User5Serializer(serializers.ModelSerializer):
    class Meta:
        model = User5
        fields = ('__all__')
