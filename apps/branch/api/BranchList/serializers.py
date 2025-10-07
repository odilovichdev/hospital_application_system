from rest_framework import serializers

from apps.branch.api.BranchCreate.serializers import BranchApplicationSerializer
from apps.branch.models import Branch


class BranchListSerializer(serializers.ModelSerializer):
    application = BranchApplicationSerializer(read_only=True)
    class Meta:
        model = Branch
        fields = (
            'id',
            'name',
            'description',
            'application',
        )

