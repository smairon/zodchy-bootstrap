import fastapi
from zodchy import codex


class Application(fastapi.FastAPI):
    cqrs_factory: codex.cqea.CQRSFactory
    identifiers_factory: codex.cqea.IdentifiersFactory
    jwt_secret: str


class Request(fastapi.Request):
    app: Application
