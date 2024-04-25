import functools

import zorge
import hermitage_alchemy
import zodchy_identity

import specs
import ports


def generic_dc(
    rdbs_dsn: str
):
    container = zorge.Container()
    identifiers_factory = zodchy_identity.UUIDIdentifiersFactory()
    container.register_dependency(
        implementation=identifiers_factory,
        contract=specs.contracts.IdentifiersFactoryContract
    )
    container.register_dependency(
        implementation=identifiers_factory.random,
        contract=specs.types.RandomIdentifierType
    )
    # -------------- Storage dependencies --------------------------------
    container.register_dependency(
        implementation=functools.partial(
            hermitage_alchemy.get_engine,
            dsn=rdbs_dsn
        ),
        contract=specs.contracts.EngineContract,
        cache_scope='container'
    )
    container.register_dependency(
        hermitage_alchemy.get_connection,
        contract=specs.contracts.WriteConnectionContract,
        cache_scope='resolver'
    )
    container.register_dependency(
        hermitage_alchemy.get_connection,
        contract=specs.contracts.ReadConnectionContract,
        cache_scope='resolver'
    )
    container.register_callback(
        contract=specs.contracts.WriteConnectionContract,
        callback=hermitage_alchemy.close_connection,
        trigger='shutdown'
    ),
    container.register_callback(
        contract=specs.contracts.ReadConnectionContract,
        callback=hermitage_alchemy.close_connection,
        trigger='shutdown'
    )
    container.register_dependency(
        contract=hermitage_alchemy.Schema,
        implementation=ports.rdbs.bootstrap_schema()
    )
    container.register_dependency(
        implementation=hermitage_alchemy.PluginRegistry(
            hermitage_alchemy.plugins.TotalPlugin,
            hermitage_alchemy.plugins.UpsertPlugin
        ),
        contract=hermitage_alchemy.PluginRegistry,
        cache_scope='resolver'
    ),
    container.register_dependency(
        implementation=hermitage_alchemy.ReadClient,
        contract=specs.contracts.ReadClientContract,
        cache_scope='resolver'
    )
    container.register_dependency(
        implementation=hermitage_alchemy.WriteClient,
        contract=specs.contracts.WriteClientContract,
        cache_scope='resolver'
    )
    return container
