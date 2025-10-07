from django.db import IntegrityError
from rest_framework import generics, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ...models import Branch
from .serializers import BranchDirectionCreateSerializer


class BranchDirectionCreateAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BranchDirectionCreateSerializer

    def post(self, request, *args, **kwargs):
        branch_id = kwargs.get('branch_id')
        branch = Branch.objects.filter(id=branch_id, application__user=request.user).first()

        if not branch:
            raise serializers.ValidationError("Branch does not exist")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save(branch=branch)
        except IntegrityError as err:
            raise serializers.ValidationError("Direction allaqachon branchda bor.") from err

        return Response(serializer.data, status=status.HTTP_201_CREATED)


__all__ = ['BranchDirectionCreateAPIView']







