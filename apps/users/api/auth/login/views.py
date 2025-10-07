from datetime import timedelta

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.utils import create_jwt_token

from .serializers import LoginSerializer


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED)

        access_token = create_jwt_token({"user_id": user.id, "email": user.email},
                                        expires_delta=timedelta(days=3))
        refresh_token = create_jwt_token({"user_id": user.id, "email": user.email},
                                         expires_delta=timedelta(days=7))

        return Response(
            {
                "access_token": access_token,
                "refresh_token": refresh_token
            }, status=status.HTTP_200_OK)


__all__ =  ["LoginAPIView"]