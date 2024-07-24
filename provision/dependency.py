import zorge
import hermitage
import hermitage_alchemy
import zodchy_security
import zodchy_identity

import settings
import specs
import ports


def generic_dc(
    jwt_secret: str,
    rdbs_dsn: str
):
    container = zorge.Container()
    identifiers_factory = zodchy_identity.UUIDIdentifiersFactory()
    container.register_dependency(
        implementation=identifiers_factory,
        contract=specs.identity.IdentifiersFactoryContract
    )
    container.register_dependency(
        implementation=identifiers_factory.random,
        contract=specs.types.RandomIdentifier
    )

    # -------------- Security dependencies ----------------------
    container.register_dependency(
        implementation=zodchy_security.JWTTokenProducer(
            issuer=settings.ISSUER,
            secret=jwt_secret,
            algorithm=settings.JWT_ALGORITHM
        ),
        contract=specs.security.AuthTokenProducerContract,
        cache_scope='container'
    )

    # -------------- Services dependencies -------------------------------
    container.register_dependency(
        implementation=hermitage.adapters.CQEA(),
        contract=hermitage.definitions.contracts.adapters.CQEAdapterContract,
        cache_scope='container'
    )

    # -------------- Storage dependencies --------------------------------
    container.register_dependency(
        hermitage_alchemy.get_engine(
            dsn=rdbs_dsn,
            debug=True,
            debug_level='INFO',
            pool_size=10
        ),
        contract=specs.connections.rdbs.EngineContract,
        cache_scope='container'
    )
    container.register_dependency(
        hermitage_alchemy.get_connection,
        contract=specs.connections.rdbs.WriteConnectionContract,
        cache_scope='resolver'
    )
    container.register_dependency(
        hermitage_alchemy.get_connection,
        contract=specs.connections.rdbs.ReadConnectionContract,
        cache_scope='resolver'
    )
    container.register_callback(
        contract=specs.connections.rdbs.WriteConnectionContract,
        callback=hermitage_alchemy.close_connection,
        trigger='shutdown'
    ),
    container.register_callback(
        contract=specs.connections.rdbs.ReadConnectionContract,
        callback=hermitage_alchemy.close_connection,
        trigger='shutdown'
    )
    container.register_dependency(
        contract=hermitage_alchemy.Schema,
        implementation=ports.rdbs.bootstrap_schema()
    )
    container.register_dependency(
        implementation=hermitage_alchemy.ReadClient,
        contract=specs.connections.rdbs.ReadClientContract,
        cache_scope='resolver'
    )
    container.register_dependency(
        implementation=hermitage_alchemy.WriteClient,
        contract=specs.connections.rdbs.WriteClientContract,
        cache_scope='resolver'
    )
    return container
