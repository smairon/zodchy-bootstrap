import uuid

from zodchy_fastapi.contracts import (
    ResponseData,
    ItemResponseModel,
    PaginatedResponseModel,
)

import specs


class ItemCreated(ResponseData):
    id: uuid.UUID


class ItemListItem(ResponseData):
    id: specs.types.IdentifierType
    name: str
    state: specs.types.ItemState


class Item(ItemResponseModel):
    external_id: specs.types.IdentifierType


class ItemCreatedResponse(ItemResponseModel):
    data: ItemCreated


class ItemListResponse(PaginatedResponseModel):
    data: list[ItemListItem]


class ItemResponse(ResponseModel):
    data: Item
