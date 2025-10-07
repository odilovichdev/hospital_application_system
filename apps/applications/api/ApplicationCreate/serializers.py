from rest_framework import serializers

from apps.applications.models import Application


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = (
            'id',
            'fullname',
            'phone_number',
            'email',
            'status'
        )
        read_only_fields = ('id', 'status')

    def create(self, validated_data):
        app = Application.objects.create(
            **validated_data,
            status=Application.Status.DRAFT
        )
        return app