import streamlord
import hermitage

import specs


async def item_reader(
    some: specs.messages.GetSomething,
    client: specs.contracts.ReadClientContract
) -> specs.messages.SomeItemReceived:
    invoice = specs.contracts.ReadInvoice(
        "acme",
        "id",
        "name",
        "external_id",
        hermitage.Clause("id", hermitage.query.EQ(some.id))
    )
    view = await client(invoice)
    data = streamlord.pipe(view.data).collect(streamlord.collectors.first)
    return specs.messages.SomeItemReceived(
        data=data
    )
