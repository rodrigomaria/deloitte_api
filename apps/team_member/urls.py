from django.urls import path

from apps.team_member.views import TeamMemberViewSet

app_name = "team_member"

urlpatterns = [
    path(
        "",
        TeamMemberViewSet.as_view({"get": "list", "post": "create"}),
        name="team_member_collection",
    ),
    path(
        "<uuid:uuid>",
        TeamMemberViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}),
        name="team_member_resource",
    ),
]
