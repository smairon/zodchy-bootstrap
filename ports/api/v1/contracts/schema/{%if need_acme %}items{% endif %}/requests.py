import uuid
from typing import Annotated

import pydantic
from zodchy_fastapi.contracts import RequestModel
from zodchy_fastapi.contracts import request
import specs


class CreateItemRequest(RequestModel):
    name: str


class ItemListRequest(RequestModel):
    id: Annotated[str | None, request.FilterParam(uuid.UUID)] = None
    name: Annotated[str | None, request.FilterParam(str)] = None
    state: Annotated[str | None, request.FilterParam(specs.types.ItemState)] = None
    order_by: Annotated[str | None, request.OrderParam("name", "id")] = None
    limit: Annotated[str | None, request.LimitParam()] = None


class UpdateItemRequest(RequestModel):
    state: specs.types.ItemState | None = pydantic.Field(None)
    name: str | None = pydantic.Field(None)
