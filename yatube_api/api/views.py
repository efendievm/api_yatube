from rest_framework import permissions, viewsets

from posts.models import Comment, Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class IsAuthorAndAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorAndAuthenticated,)

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs['post_id'])


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorAndAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
