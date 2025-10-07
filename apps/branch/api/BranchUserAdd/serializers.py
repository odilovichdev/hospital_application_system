from typing import Any, ClassVar

from rest_framework import serializers

from apps.branch.models import BranchUser


class BranchUserAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchUser
        fields = ('user',)
        extra_kwargs: ClassVar[dict[str, Any]] = {
            "user": {'write_only': True}
        }

