import hermitage

import specs


async def creation_writer(
    message: specs.messages.ItemLinkedWithExternalService,
    client: specs.contracts.WriteClientContract
):
    invoice = specs.contracts.WriteInvoice(
        "items",
        hermitage.Row(
            id=message.id,
            name=message.name,
            external_id=message.external_id
        )
    )
    await client(invoice)
