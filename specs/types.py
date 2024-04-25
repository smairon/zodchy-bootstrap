import typing
import enum
import uuid
import zodchy

NoValueType = zodchy.codex.NoValueType
IdentifierType = uuid.UUID
RandomIdentifierType = typing.NewType("RandomIdentifier", uuid.UUID)


class SomeKind(str, enum.Enum):
    big = "big"
    small = "small"


class AcmeState(str, enum.Enum):
    new = "new"
    active = "active"
    deactivated = "deactivated"
