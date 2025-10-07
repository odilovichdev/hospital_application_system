from rest_framework import serializers

from apps.branch.models import BranchEquipment


class BranchEquipmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BranchEquipment
        fields = ('id', 'equipment')




