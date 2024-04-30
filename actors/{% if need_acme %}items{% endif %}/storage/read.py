import streamlord
import hermitage

import specs


async def item_reader(
    item: specs.messages.GetItem,
    client: specs.contracts.ReadClientContract
) -> specs.messages.ItemReceived:
    invoice = specs.contracts.ReadInvoice(
        "items",
        "id",
        "name",
        "external_id",
        hermitage.Clause("id", hermitage.query.EQ(item.id))
    )
    view = await client(invoice)
    data = streamlord.pipe(view.data).collect(streamlord.collectors.first)
    return specs.messages.ItemReceived(
        data=data
    )
