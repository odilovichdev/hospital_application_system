from typing import ClassVar

from django.db import IntegrityError
from rest_framework import generics, serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ...models import BranchDirection
from .serializers import BranchUserAssignSerializer


class BranchUserAssignAPIVIew(generics.GenericAPIView):
    permission_classes: ClassVar[list] = [IsAuthenticated]
    serializer_class = BranchUserAssignSerializer

    def post(self, request, *args, **kwargs):
        branch_direction_id = kwargs.get('branch_direction_id')

        branch_direction = get_object_or_404(
            BranchDirection.objects.select_related('branch', 'direction'),
            id=branch_direction_id,
            branch__application__user=request.user
        )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(branch_direction=branch_direction)
        except IntegrityError as err:
            raise serializers.ValidationError("Bu user Directionda bor.") from err

        return Response(
            {"detail": "User successfully assigned to branch direction."},
            status=status.HTTP_201_CREATED
        )


__all__ = ['BranchUserAssignAPIVIew']