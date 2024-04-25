import dataclasses
import uuid


@dataclasses.dataclass
class RequestAuthContext:
    user_id: uuid.UUID
