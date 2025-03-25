from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'content', 'status', 'created_at']
        extra_kwargs = {
            'user': {
                'help_text': 'ID of the user this task belongs to (optional)'
            }
        }

    def create(self, validated_data):
        if 'user' not in validated_data:
            validated_data['user'] = self.context['request'].user
        return super().create(validated_data)