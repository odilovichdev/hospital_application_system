from django.db import IntegrityError
from rest_framework import generics, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ...models import BranchDirection
from .serializers import BranchEquipmentCreateSerializer


class BranchEquipmentCreateAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BranchEquipmentCreateSerializer

    def post(self, request, *args, **kwargs):
        branch_direction_id = kwargs.get('branch_direction_id')
        branch_direction = BranchDirection.objects.filter(
            id=branch_direction_id,
            branch__application__user=request.user
        ).first()

        if not branch_direction:
            raise serializers.ValidationError("Branch direction does not exist or access denied.")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save(branch_direction=branch_direction)
        except IntegrityError as err:
            raise serializers.ValidationError('Bu texnika allaqachon shu direction uchun biriktirilgan.') from err

        return Response(serializer.data, status=status.HTTP_201_CREATED)


__all__ = ['BranchEquipmentCreateAPIView']