import uuid
import specs


async def create_item_context(
    message: specs.messages.CreateItem
) -> specs.context.CreateItemAuditContext:
    # get some information about desired user
    # owner_id = some_client.get_owner_id(message.name)
    return specs.context.CreateItemAuditContext(
        user_id=uuid.uuid4()
    )
