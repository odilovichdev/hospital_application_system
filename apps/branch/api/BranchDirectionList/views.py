from typing import ClassVar

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...models import BranchDirection
from .serializers import BranchDirectionSerializer


class BranchDirectionListAPIView(generics.ListAPIView):
    serializer_class = BranchDirectionSerializer
    permission_classes: ClassVar[list] = [IsAuthenticated]

    def get_queryset(self):
        branch_id = self.kwargs.get('branch_id')
        return BranchDirection.objects.filter(branch_id=branch_id)


__all__ =['BranchDirectionListAPIView']
