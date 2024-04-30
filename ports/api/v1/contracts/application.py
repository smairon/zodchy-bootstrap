import fastapi
import specs


class Application(fastapi.FastAPI):
    cqrs_factory: specs.contracts.CQRSFactoryContract
    identifiers_factory: specs.contracts.IdentifiersFactoryContract
    jwt_secret: str


class Request(fastapi.Request):
    app: Application
