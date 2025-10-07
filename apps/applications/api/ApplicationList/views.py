from django.db.models import Q
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ...models import Application
from .serializers import ApplicationListSerializer


class ApplicationListView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ApplicationListSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Application.objects.filter(
                Q(status=Application.Status.SUBMITTED) |
                Q(status=Application.Status.REVIEW) |
                Q(status=Application.Status.APPROVED)
            )
        return Application.objects.filter(user=user)


__all__ = ['ApplicationListView']



