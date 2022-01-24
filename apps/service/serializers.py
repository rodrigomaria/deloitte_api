from rest_framework import serializers
from rest_framework.serializers import DateTimeField

from apps.service.repositories import service_repository


class ServiceSerializer(serializers.ModelSerializer):
    created = DateTimeField()
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=256, required=True)

    class Meta:
        model = service_repository.model
        fields = ["uuid", "created", "title", "description"]
        read_only_fields = [
            "uuid",
            "created",
        ]


class ServiceCreateSerializer(ServiceSerializer):
    class Meta:
        model = service_repository.model
        fields = ["title", "description"]
        read_only_fields = [
            "uuid",
            "created",
        ]
