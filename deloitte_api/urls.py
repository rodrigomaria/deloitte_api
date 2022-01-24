"""deloitte_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urls = [
    path("post/", include("apps.post.urls", namespace="post")),
    path("service/", include("apps.service.urls", namespace="service")),
    path("team_member/", include("apps.team_member.urls", namespace="team_member")),
]

urlpatterns = [
    path("deloitte/api/", include(urls)),
    path("deloitte/api/admin/", admin.site.urls),
    path("deloitte/api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Path to see in browser the all routes (swaggger)
    path(
        "",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]
