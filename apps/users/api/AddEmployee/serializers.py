from rest_framework import serializers

from apps.users.models import Employee


class AddEmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'email', 'fullname')