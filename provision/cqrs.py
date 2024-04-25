import pancho
from .dependency import generic_dc


def generic_cqrs(
    db_pool_dsn: str,
    actors_registry: pancho.definition.contracts.ActorRegistry
):
    return pancho.CQRSFactory(
        di_container=generic_dc(
            rdbs_dsn=db_pool_dsn
        ),
        actor_registry=actors_registry
    )
