from rest_framework import serializers
from rest_framework.serializers import DateTimeField

from apps.post.repositories import post_repository


class PostSerializer(serializers.ModelSerializer):
    created = DateTimeField()
    content = serializers.CharField(max_length=256, required=True)

    class Meta:
        model = post_repository.model
        fields = [
            "uuid",
            "created",
            "content",
        ]
        read_only_fields = [
            "uuid",
            "created",
        ]


class PostCreateSerializer(PostSerializer):
    class Meta:
        model = post_repository.model
        fields = ["content"]
        read_only_fields = [
            "uuid",
            "created",
        ]
