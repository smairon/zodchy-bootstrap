import asyncio

import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncConnection, create_async_engine
from faker import Faker
from . import schema


class Seeder:
    def __init__(
        self,
        connection: AsyncConnection,
        faker: Faker
    ):
        self._connection = connection
        self._faker = faker

    async def __call__(self):
        await self._truncate_all()
        await self._seed()

    async def _seed(
        self
    ):
        pass

    async def _truncate_all(
        self,
    ):
        for table in schema.db_metadata.tables.values():
            table_name = table.name
            if table_name != 'alembic_version':
                await self._connection.execute(sqlalchemy.sql.text(f"TRUNCATE TABLE {table_name} CASCADE"))


async def seed(dsn: str):
    engine = create_async_engine(url=dsn)
    async with engine.begin() as connection:
        await Seeder(connection=connection, faker=Faker(locale='ru_RU'))()


def process(dsn: str):
    asyncio.run(seed(dsn))
