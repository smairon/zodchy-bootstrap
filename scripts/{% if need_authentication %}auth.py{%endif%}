import uuid

import settings
from zodchy_security import JWTTokenProducer
from specs.configs.security import JWTConfig


def generate_access_token(user_id: str, lifetime: int = 86400) -> str:
    return JWTTokenProducer(
        secret=JWTConfig().jwt_secret_value,
        algorithm=settings.JWT_ALGORITHM,
        issuer=settings.ISSUER
    ).access_token(user_id=uuid.UUID(user_id), lifetime_in_seconds=lifetime)
