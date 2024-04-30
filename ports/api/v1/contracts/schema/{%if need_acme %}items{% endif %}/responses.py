import uuid

from zodchy_fastapi.contracts import (
    ResponseModel,
    PaginatedResponseModel,
    DataModel
)

import specs


class ItemCreated(DataModel):
    id: uuid.UUID


class ItemListItem(DataModel):
    id: specs.types.IdentifierType
    name: str
    state: specs.types.ItemState


class Item(ItemListItem):
    external_id: specs.types.IdentifierType


class ItemCreatedResponse(ResponseModel):
    data: ItemCreated


class ItemListResponse(PaginatedResponseModel):
    data: list[ItemListItem]


class ItemResponse(ResponseModel):
    data: Item
