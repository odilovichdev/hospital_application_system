from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import DirectionCreateSerializer


class DirectionCreateAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DirectionCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


__all__ = ['DirectionCreateAPIView']





