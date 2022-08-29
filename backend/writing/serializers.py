from rest_framework import serializers
from .models import Writing

class WritingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
            'inittime',
            'board',
        )
        model = Writing