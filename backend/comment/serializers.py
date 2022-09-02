from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'post_id',
            'content',
            'inittime',
        )
        model = Comment