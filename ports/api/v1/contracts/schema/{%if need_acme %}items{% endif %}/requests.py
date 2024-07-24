import uuid
from typing import Annotated

import pydantic
import specs
from zodchy_fastapi.request.schema import (
    RequestModel,
    FilterParam,
    OrderParam,
    LimitParam
)


class CreateItemRequest(RequestModel):
    name: str


class ItemListRequest(RequestModel):
    id: Annotated[str | None, FilterParam(uuid.UUID)] = None
    name: Annotated[str | None, FilterParam(str)] = None
    state: Annotated[str | None, FilterParam(specs.types.ItemState)] = None
    order_by: Annotated[str | None, OrderParam("name", "id")] = None
    limit: Annotated[str | None, LimitParam()] = None


class UpdateItemRequest(RequestModel):
    state: specs.types.ItemState | None = pydantic.Field(None)
    name: str | None = pydantic.Field(None)
