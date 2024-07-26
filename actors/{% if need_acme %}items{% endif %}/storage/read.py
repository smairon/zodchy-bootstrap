import streamlord
import hermitage
import hermitage_alchemy

import specs


async def item_reader(
    query: specs.messages.GetItem,
    client: specs.connections.rdbs.ReadClientContract
) -> specs.messages.ItemReceived:
    invoice = specs.patterns.ReadInvoice(
        "items",
        "id",
        "name",
        "external_id",
        "state_id",
        hermitage.Clause("id", hermitage.query.EQ(query.id))
    )
    view = await client(invoice)
    data = streamlord.pipe(view.data).map(
        streamlord.mappers.Injector(
            specs.mappings.rdbs.item_state,
            "state_id",
            "state",
            True
        )
    ).collect(streamlord.collectors.first)
    return specs.messages.ItemReceived(
        data=data
    )


async def list_reader(
    query: specs.messages.GetItems,
    client: specs.contracts.ReadClientContract
) -> specs.messages.ItemsReceived:
    invoice = specs.contracts.ReadInvoice(
        "items",
        "id",
        "name",
        "external_id",
        "state_id",
        *hermitage.QueryParser(
            query
        ).map(
            hermitage.mappers.ClauseInjector(
                specs.mappings.rdbs.item_state,
                "state",
                "state_id"
            )
        ),
        hermitage_alchemy.plugins.total.Beacon()
    )
    view = await client(invoice)
    data = streamlord.pipe(view.data).map(
        streamlord.mappers.Injector(
            specs.mappings.rdbs.item_state,
            "state_id",
            "state",
            True
        )
    ).collect(list)
    return specs.messages.ItemsReceived(
        data=data,
        total=view.meta.get('total')
    )

