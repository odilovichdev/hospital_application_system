from rest_framework import serializers

from apps.branch.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'fullname',
            'created_at',
            'updated_at'
        )