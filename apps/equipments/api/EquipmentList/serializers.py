from rest_framework import serializers

from apps.equipments.models import Equipment


class EquipmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = (
            'id',
            'name',
            'description'
        )