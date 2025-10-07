from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ...models import Application
from .serializers import ApplicationDetailSerializer


class ApplicationDetailView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationDetailSerializer

    def get(self, request, *args, **kwargs):
        app_id = kwargs.get('application_id')
        app = get_object_or_404(Application, id=app_id)
        serializer = self.get_serializer(app)
        return Response(serializer.data, status=status.HTTP_200_OK)


__all__ = ['ApplicationDetailView']
