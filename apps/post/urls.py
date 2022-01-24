from django.urls import path

from apps.post.views import PostViewSet

app_name = "post"

urlpatterns = [
    path(
        "",
        PostViewSet.as_view({"get": "list", "post": "create"}),
        name="post_collection",
    ),
    path(
        "<uuid:uuid>",
        PostViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}),
        name="post_resource",
    ),
]
