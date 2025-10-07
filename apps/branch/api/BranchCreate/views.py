from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.applications.models import Application

from .serializers import BranchCreateSerializer


class BranchCreateAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BranchCreateSerializer

    def post(self, request, *args, **kwargs):
        app_id = kwargs.get('application_id')
        app = get_object_or_404(Application, id=app_id)

        serializer = self.get_serializer(data=request.data, context={'app': app, 'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(application=app)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


__all__ = ['BranchCreateAPIView']