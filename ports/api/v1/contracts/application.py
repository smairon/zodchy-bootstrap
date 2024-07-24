import specs
import zodchy_fastapi


class Application(zodchy_fastapi.contracts.Application):
    cqrs_factory: specs.services.CQRSFactoryContract
    identifiers_factory: specs.contracts.IdentifiersFactoryContract
    jwt_secret: str


class Request(zodchy_fastapi.contracts.Request):
    app: Application
