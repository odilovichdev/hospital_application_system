from typing import ClassVar

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.branch.models import BranchDirection, BranchUser

from .serializers import BranchUserListSerializer


class BranchUserListAPIView(generics.GenericAPIView):
    permission_classes: ClassVar[list] = [IsAuthenticated]
    serializer_class = BranchUserListSerializer

    def get(self, request, *args, **kwargs):
        branch_direction_id = kwargs.get('branch_direction_id')
        branch_direction = get_object_or_404(
            BranchDirection,
            id=branch_direction_id,
            branch__application__user=request.user
        )

        branch_users = BranchUser.objects.filter(branch_direction=branch_direction).select_related('user')
        serializer = self.get_serializer(branch_users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


__all__ = ['BranchUserListAPIView']
