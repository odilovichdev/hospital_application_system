from typing import ClassVar

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import AddEmployeeCreateSerializer


class AddEmployeeCreateAPIView(generics.GenericAPIView):
    permission_classes: ClassVar[list] = [IsAuthenticated]
    serializer_class = AddEmployeeCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(status=status.HTTP_201_CREATED)


__all__ = ['AddEmployeeCreateAPIView']




