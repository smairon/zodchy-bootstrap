import uuid
from typing import Annotated

import pydantic
from zodchy_fastapi.contracts import RequestModel
from zodchy_fastapi.contracts import request
import specs


class SomethingCreateRequest(RequestModel):
    name: str


class SomethingListRequest(RequestModel):
    id: Annotated[str | None, request.FilterParam(uuid.UUID)] = None
    name: Annotated[str | None, request.FilterParam(str)] = None
    state: Annotated[str | None, request.FilterParam(specs.types.AcmeState)] = None
    order_by: Annotated[str | None, request.OrderParam("name", "id")] = None
    limit: Annotated[str | None, request.LimitParam()] = None


class SomethingUpdateRequest(RequestModel):
    state: specs.types.AcmeState | None = pydantic.Field(None)
    name: str | None = pydantic.Field(None)
