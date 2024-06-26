import typing
import collections.abc

import zodchy_fastapi

from zodchy import codex

IdentifiersFactoryContract = codex.identity.IdentifiersFactory


class CQRSFactoryContract(typing.Protocol):
    async def get_processor(
        self,
        context: collections.abc.Mapping[typing.Any, typing.Any] | None = None
    ): ...


QueryAdapterContract = zodchy_fastapi.contracts.RequestModelAdapter
