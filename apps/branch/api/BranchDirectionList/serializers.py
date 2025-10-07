from typing import ClassVar

from rest_framework import serializers

from apps.branch.models import BranchDirection
from apps.directions.models import Direction


class BranchDirectionDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields: ClassVar[list[str]] = ['id', 'name', 'description']


class BranchDirectionSerializer(serializers.ModelSerializer):
    direction = BranchDirectionDirectionSerializer(read_only=True)

    class Meta:
        model = BranchDirection
        fields: ClassVar[list[str]] = ['id', 'direction']

