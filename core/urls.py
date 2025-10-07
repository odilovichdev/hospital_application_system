from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/v1/auth/", include("apps.users.urls", namespace="users")),
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
    path("api/v1/branches/", include("apps.branch.urls", namespace="branch")),
    path("api/v1/equipments/", include("apps.equipments.urls", namespace="equipments")),
    path("api/v1/directions/", include("apps.directions.urls", namespace="directions")),
    path("api/v1/applications/", include("apps.applications.urls", namespace="application")),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
