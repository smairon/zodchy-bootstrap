import typing
import orjson
import fastapi

from functools import singledispatch
from asyncpg import Record
from asyncpg.pgproto.pgproto import UUID
from fastapi.responses import JSONResponse, Response


@singledispatch
def convert(value):
    raise TypeError(f'Unserializable value: {value!r}')


@convert.register(Record)
def convert_asyncpg_record(value: Record):
    return dict(value)


@convert.register(UUID)
def convert_asyncpg_uuid(value: UUID):
    return str(value)


class EmptyResponse(Response):
    pass


class ORJSONResponse(JSONResponse):
    def render(self, content: typing.Any) -> bytes:
        return orjson.dumps(
            content,
            option=orjson.OPT_NON_STR_KEYS | orjson.OPT_SERIALIZE_NUMPY,
            default=convert
        )


Embedded = fastapi.Depends
