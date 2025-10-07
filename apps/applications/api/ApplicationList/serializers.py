from rest_framework import serializers

from apps.applications.models import Application


class ApplicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            'id',
            'application_number',
            'fullname',
            'phone_number',
            'email',
            'status'
        )

