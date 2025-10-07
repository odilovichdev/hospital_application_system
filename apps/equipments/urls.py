from django.urls import path

from apps.equipments.api import (
    EquipmentCreateAPIView,
    EquipmentListAPIView,
)

app_name = 'equipments'


urlpatterns = [
    path('', EquipmentListAPIView.as_view(), name='equipment-list'),
    path('create/', EquipmentCreateAPIView.as_view(), name='equipment-create'),
]