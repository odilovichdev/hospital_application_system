from rest_framework import serializers

from apps.directions.models import Direction


class DirectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = (
            "id",
            "name",
            "description"
        )