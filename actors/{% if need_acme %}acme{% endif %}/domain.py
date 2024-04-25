import uuid

import specs


async def create(
    message: specs.messages.CreateSomething,
) -> specs.messages.SomethingCreated:
    # Place here any business domain logic
    return specs.messages.SomethingCreated(
        id=uuid.uuid4(),
        name=message.name
    )
