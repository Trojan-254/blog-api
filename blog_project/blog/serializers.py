from rest_framework import serializers
from . models import Comment


class CommentSerializer(serializers.ModelSerializer):
    '''handle comment serializer'''
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'author']
