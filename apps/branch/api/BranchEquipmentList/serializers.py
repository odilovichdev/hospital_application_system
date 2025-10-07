from rest_framework import serializers

from apps.branch.models import BranchEquipment
from apps.equipments.models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'name', 'description')


class BranchEquipmentListSerializer(serializers.ModelSerializer):
    equipment = EquipmentSerializer()

    class Meta:
        model = BranchEquipment
        fields = ('id', 'equipment')
