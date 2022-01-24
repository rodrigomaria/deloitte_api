from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.team_member.repositories import team_member_repository
from apps.team_member.serializers import TeamCreateSerializer, TeamMemberSerializer


class TeamMemberViewSet(GenericViewSet):
    serializer_class = TeamMemberSerializer
    lookup_field = "uuid"
    # UUID4 regex
    lookup_value_regex = "[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"

    def create(self, request):
        serializer = TeamCreateSerializer(
            data={
                **request.data,
            }
        )
        if serializer.is_valid():
            created_team_member = team_member_repository.create(
                name=serializer.data["name"],
                function=serializer.data["function"],
                address=serializer.data["address"],
                mobile=serializer.data["mobile"],
            )
            read_serializer = self.serializer_class(created_team_member)
            return Response(status=status.HTTP_201_CREATED, data=read_serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def update(self, request, uuid, partial=False):
        instance = team_member_repository.get_by_uuid(uuid)
        serializer = TeamCreateSerializer(
            instance,
            data={
                **request.data,
            },
            partial=partial,
        )
        if serializer.is_valid():
            updated_team_member = serializer.save()
            read_serializer = self.serializer_class(updated_team_member)
            return Response(data=read_serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def retrieve(self, request, uuid):
        instance = team_member_repository.get_by_uuid(uuid)
        serializer = self.serializer_class(instance)
        return Response(data=serializer.data)

    def partial_update(self, request, uuid):
        return self.update(request, uuid, partial=True)

    def destroy(self, request, uuid):
        team_member_repository.delete(uuid)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        queryset = team_member_repository.get_all()
        serializer = self.serializer_class(
            queryset,
            many=True,
        )
        return Response(data=serializer.data)
