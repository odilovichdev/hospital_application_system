from django.urls import path

from apps.applications.api import (
    ApplicationCreateView,
    ApplicationDetailView,
    ApplicationListView,
    ApplicationStatusUpdateAPIView,
)

app_name = "applications"

urlpatterns = [
    path('<int:application_id>', ApplicationDetailView.as_view(), name='application-detail'),
    path('<int:pk>/change-status', ApplicationStatusUpdateAPIView.as_view(), name='change-status'),
    path("create", ApplicationCreateView.as_view(), name="application_create"),
    path("list", ApplicationListView.as_view(), name="application_list"),
]