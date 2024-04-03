from rest_framework import serializers

from posts.models import Comment, Group, Post
from .mixins import IncludeAuthorMixin


class CommentSerializer(IncludeAuthorMixin):
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', "created")
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializer(IncludeAuthorMixin):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group')
        model = Post
