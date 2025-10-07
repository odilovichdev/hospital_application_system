from typing import ClassVar

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.api.EmployeeList.serializers import EmployeeListSerializer
from apps.users.models import Employee


class EmployeeListAPIView(generics.GenericAPIView):
    permission_classes: ClassVar[list] = [IsAuthenticated]
    serializer_class = EmployeeListSerializer

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.filter(
            user=request.user
        )

        serializer = self.get_serializer(employees, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)


__all__ = ['EmployeeListAPIView']
