from rest_framework import serializers
from .models import Writing

import os
from comment.serializers import CommentSerializer

class WritingSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        fields = (
            'id',
            'title',
            'content',
            'inittime',
            'board',
            'comments',
        )
        model = Writing

