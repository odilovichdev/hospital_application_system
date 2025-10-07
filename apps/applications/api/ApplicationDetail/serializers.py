from rest_framework import serializers

from apps.applications.models import Application


class ApplicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            'id',
            'fullname',
            'phone_number',
            'email',
            'status',
            'created_at'
        )