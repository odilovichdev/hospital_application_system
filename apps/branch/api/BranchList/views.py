from rest_framework import generics, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.applications.models import Application

from .serializers import BranchListSerializer


class BranchListAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BranchListSerializer

    def get(self, request, *args, **kwargs):
        app_id = kwargs.get('application_id')
        app = Application.objects.filter(id=app_id, user=request.user).first()

        if not app:
            raise serializers.ValidationError({"detail": "Application Not Found."})

        branches = app.branches.all()

        serializer = self.get_serializer(branches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


__all__ = ['BranchListAPIView']

