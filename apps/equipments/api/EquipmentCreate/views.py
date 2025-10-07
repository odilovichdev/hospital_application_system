from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import EquipmentCreateSerializer


class EquipmentCreateAPIView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EquipmentCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


__all__ = ['EquipmentCreateAPIView']