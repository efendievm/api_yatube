from rest_framework import serializers


class IncludeAuthorMixin(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
