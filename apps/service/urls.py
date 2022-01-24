from django.urls import path

from apps.service.views import ServiceViewSet

app_name = "service"

urlpatterns = [
    path(
        "",
        ServiceViewSet.as_view({"get": "list", "post": "create"}),
        name="service_collection",
    ),
    path(
        "<uuid:uuid>",
        ServiceViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}),
        name="service_resource",
    ),
]
