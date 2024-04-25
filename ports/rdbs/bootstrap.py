import hermitage_alchemy
from . import schema


def bootstrap_schema() -> hermitage_alchemy.Schema:
    return hermitage_alchemy.Schema(
        tables=schema.db_metadata.tables.values()
    )