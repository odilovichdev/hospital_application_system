from rest_framework import serializers

from apps.branch.models import BranchDirection


class BranchDirectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchDirection
        fields = (
            'id',
            'branch',
            'direction'
        )
        read_only_fields = ('id', 'branch')
