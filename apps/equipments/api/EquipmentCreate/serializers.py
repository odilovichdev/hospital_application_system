from rest_framework import serializers

from apps.equipments.models import Equipment


class EquipmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = (
            'id',
            'name',
            'description'
        )