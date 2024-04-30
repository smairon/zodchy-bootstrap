import zodchy_fastapi
from fastapi.exceptions import RequestValidationError

import specs
from . import (
    routes,
    contracts,
    middleware,
)


def api(
    cqrs_factory: specs.contracts.CQRSFactoryContract,
    jwt_secret: str
) -> contracts.Application:
    api_app = contracts.Application()
    api_app = _bootstrap_exception_handlers(api_app)
    api_app.middleware('http')(middleware.auth)
    api_app.include_router(_bootstrap_router())
    api_app.jwt_secret = jwt_secret
    api_app.cqrs_factory = cqrs_factory
    return api_app


def _bootstrap_router(api_version: str = 'v1'):
    if api_version == 'v1':
        router = routes.v1
        return router


def _bootstrap_exception_handlers(
    api_app: contracts.Application
) -> contracts.Application:
    api_app.add_exception_handler(
        RequestValidationError,
        zodchy_fastapi.handlers.validation_exception_handler
    )
    api_app.add_exception_handler(
        Exception,
        zodchy_fastapi.handlers.generic_exception_handler
    )
    return api_app
