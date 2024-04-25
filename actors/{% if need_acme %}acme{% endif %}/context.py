import uuid
import specs


async def create_something_context(
    message: specs.messages.CreateSomething
) -> specs.context.CreateSomethingAuditContext:
    # get some information about desired user
    # owner_id = some_client.get_owner_id(message.name)
    owner_id = message.owner_id
    return specs.context.CreateSomethingAuditContext(
        user_id=uuid.uuid4()
    )
