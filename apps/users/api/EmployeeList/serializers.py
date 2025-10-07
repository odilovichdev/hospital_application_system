from rest_framework import serializers

from apps.users.models import Employee


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            "email",
            'fullname'
        )