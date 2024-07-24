import typing
from . import types


class AuthTokenProducerContract(typing.Protocol):
    def access_token(self, user_id: types.UserId, lifetime_in_seconds: int = 300): ...

    def refresh_token(self): ...
