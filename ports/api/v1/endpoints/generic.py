import zodchy
import zodchy_patterns

import specs
import settings
from .. import contracts


async def execute_command(
    message: zodchy.codex.cqea.Command,
    request: contracts.Request
):
    async with request.app.cqrs_factory.get_processor(
        context={specs.context.RequestAuthContext: _build_auth_context(request)}
    ) as cp:
        return await cp(message)


def _build_auth_context(request: contracts.Request) -> specs.context.RequestAuthContext:
    return specs.context.RequestAuthContext(
        user_id=request.scope.get('user_id') or settings.SYSTEM_USER
    )


def format_response(
    stream: zodchy.codex.cqea.EventStream
):
    data = None
    for event in filter(lambda x: isinstance(x, zodchy_patterns.events.HttpEvent), stream):
        data = event
        if isinstance(event, zodchy_patterns.events.HttpError):
            break
    if data:
        if data.get_content() is None:
            return contracts.payload.EmptyResponse(status_code=data.get_status_code())
        else:
            return contracts.payload.ORJSONResponse(
                status_code=data.get_status_code(),
                content=data.get_content()
            )
    else:
        return contracts.payload.EmptyResponse(status_code=200)
