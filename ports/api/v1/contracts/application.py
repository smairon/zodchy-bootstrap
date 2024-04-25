import fastapi
import zodchy


class Application(fastapi.FastAPI):
    cqrs_factory: zodchy.codex.CQRSFactory
    identifiers_factory: zodchy.codex.IdentifiersFactory
    jwt_secret: str


class Request(fastapi.Request):
    app: Application
