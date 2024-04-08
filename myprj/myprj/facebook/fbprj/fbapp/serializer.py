from rest_framework import serializers
from .models import Post, Like , Comment

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

   

    

class LikeSerializer(serializers.Serializer):
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())



class CommentSerializer(serializers.Serializer):
    post_id = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

