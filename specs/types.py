import typing
import enum
import uuid
import zodchy

Empty = zodchy.types.Empty
IdentifierType = uuid.UUID
RandomIdentifierType = typing.NewType("RandomIdentifier", uuid.UUID)


class SomeKind(str, enum.Enum):
    big = "big"
    small = "small"


class ItemState(str, enum.Enum):
    new = "new"
    active = "active"
    deactivated = "deactivated"
