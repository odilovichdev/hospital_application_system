from typing import ClassVar

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.applications.models import Application

from .serializers import ApplicationStatusUpdateSerializer


class ApplicationStatusUpdateAPIView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationStatusUpdateSerializer
    permission_classes: ClassVar[list] = [IsAuthenticated]


__all__ = ['ApplicationStatusUpdateAPIView']
