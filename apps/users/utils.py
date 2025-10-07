from datetime import UTC, datetime, timedelta

from django.conf import settings
from jose import JWTError, jwt


def create_jwt_token(data: dict, expires_delta: timedelta | None= None) -> str:
    to_ecode = data.copy()
    delta = (
        timedelta(minutes=expires_delta.total_seconds())
        if expires_delta
        else timedelta(minutes=15)
    )

    expires_time = datetime.now(UTC) + delta
    to_ecode.update({"exp": expires_time})
    encoded_jwt = jwt.encode(to_ecode, settings.SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def decode_jwt_token(token:str) -> dict | None:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

        exp_timestamp = payload.get("exp")
        exp_datetime = datetime.fromtimestamp(exp_timestamp, tz=UTC)
        return payload if exp_datetime >= datetime.now(UTC) else None
    except JWTError:
        return None