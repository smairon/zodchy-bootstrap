import specs
import actors
import provision

from ports.api import v1


def app_v1():
    db_pool_config = specs.configs.storage.rdbs.DBPoolConfig()
    encryption_config = specs.configs.security.JWTConfig()
    return v1.bootstrap.api(
        cqrs_factory=provision.generic_cqrs(
            db_pool_dsn=db_pool_config.dsn,
            actors_registry=actors.bootstrap.registry()
        ),
        jwt_secret=encryption_config.jwt_secret_value,
        query_adapter=provision.query_adapter
    )
