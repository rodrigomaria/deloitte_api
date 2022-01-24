from rest_framework import serializers
from rest_framework.serializers import DateTimeField

from apps.team_member.repositories import team_member_repository


class TeamMemberSerializer(serializers.ModelSerializer):
    created = DateTimeField()
    name = serializers.CharField(max_length=100, required=True)
    function = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = team_member_repository.model
        fields = ["uuid", "created", "name", "function", "address", "mobile"]
        read_only_fields = [
            "uuid",
            "created",
        ]


class TeamCreateSerializer(TeamMemberSerializer):
    class Meta:
        model = team_member_repository.model
        fields = ["name", "function", "address", "mobile"]
        read_only_fields = [
            "uuid",
            "created",
        ]
