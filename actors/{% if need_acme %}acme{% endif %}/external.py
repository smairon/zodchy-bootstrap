import uuid

import specs


async def call_some_service(
    message: specs.messages.SomethingCreated,
) -> specs.messages.SomethingLinkedWithExternalService:
    try:
        # try to call external service
        # external_id = some_service.get_id(id=message.id)
        external_id = uuid.uuid4()
        return specs.messages.SomethingLinkedWithExternalService(
            id=message.id,
            name=message.name,
            external_id=external_id
        )
    except Exception:
        return specs.messages.LinkingSomethingFailed()
