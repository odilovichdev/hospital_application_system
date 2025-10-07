from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from .utils import decode_jwt_token  # token funksiyang joylashgan joydan import qilasan

User = get_user_model()

class JWTAuthentication(BaseAuthentication):
    keyword = "Bearer"

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith(self.keyword):
            return None

        token = auth_header[len(self.keyword):].strip()
        payload = decode_jwt_token(token)

        if payload is None:
            raise exceptions.AuthenticationFailed("Invalid or expired token")

        user_id = payload.get("user_id")
        if not user_id:
            raise exceptions.AuthenticationFailed("Invalid payload: user_id missing")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("User not found") from None

        return (user, None)
