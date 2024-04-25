import uuid

from zodchy_fastapi.contracts import (
    ResponseModel,
    PaginatedResponseModel,
    DataModel
)

import specs


class SomethingCreated(DataModel):
    id: uuid.UUID


class SomethingListItem(DataModel):
    id: specs.types.IdentifierType
    name: str
    state: specs.types.AcmeState


class Something(SomethingListItem):
    external_id: specs.types.IdentifierType


class SomethingCreatedResponse(ResponseModel):
    data: SomethingCreated


class SomethingListResponse(PaginatedResponseModel):
    data: list[SomethingListItem]


class SomethingItemResponse(ResponseModel):
    data: Something
