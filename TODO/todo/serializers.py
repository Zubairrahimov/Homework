from rest_framework import serializers
from .models import TodoModel

class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('taskname', 'created', 'updated', 'status', 'description', 'due_date' , 'user')


    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(TodoModelSerializer, self).create(validated_data)
    