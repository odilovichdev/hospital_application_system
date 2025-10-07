from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.directions.models import Direction

from .serializers import DirectionListSerializer


class DirectionListAPIView(generics.GenericAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        directions = self.get_queryset()
        serializer = self.get_serializer(directions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


__all__ = ['DirectionListAPIView']
