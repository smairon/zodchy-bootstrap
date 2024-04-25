import jwt
import uuid

import fastapi
import settings
from ..contracts.application import Request

access_denied_response = fastapi.responses.ORJSONResponse(
    status_code=403,
    content={
        'detail': 'Access denied'
    }
)


async def auth(request: Request, call_next):
    for public_path in settings.OPENED_PATHS:
        if request.url.path.startswith(public_path):
            return await call_next(request)

    access_token = request.headers.get('Authorization', '').replace('Bearer', '').strip()
    if not access_token:
        return access_denied_response

    try:
        payload = jwt.decode(
            access_token,
            request.app.jwt_secret,
            algorithms=[settings.JWT_ALGORITHM]
        )
    except jwt.exceptions.PyJWTError:
        return access_denied_response

    if not payload:
        return access_denied_response

    request.scope['user_id'] = uuid.UUID(payload.get('user_id'))

    return await call_next(request)
