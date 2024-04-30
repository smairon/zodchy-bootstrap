import uuid

import specs


async def create(
    message: specs.messages.CreateItem,
) -> specs.messages.ItemCreated:
    # Place here any business domain logic
    return specs.messages.ItemCreated(
        id=uuid.uuid4(),
        name=message.name
    )
