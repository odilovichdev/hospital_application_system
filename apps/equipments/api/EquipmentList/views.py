from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.equipments.models import Equipment

from .serializers import EquipmentListSerializer


class EquipmentListAPIView(generics.GenericAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        equipments = self.get_queryset()
        serializer = self.get_serializer(equipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


__all__ = ['EquipmentListAPIView']