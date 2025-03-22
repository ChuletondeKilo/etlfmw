from pydantic import BaseModel, field_validator
from typing import Type, TypeVar, Optional
from enum import Enum
from .utils import connection_types, registered_schema_types, register_connection_type, EnvironmentCollectionNameEnum

class TypingConfig(BaseModel):

    class Config:
        extra = 'forbid'

@register_connection_type
class PostgresConnectionSchema(TypingConfig):

    host: str
    port: int
    dbname: str
    user: str
    password: str

if len(registered_schema_types) == 1:
    ConnectionsSchemaList = TypeVar('ConnectionsSchemaList', bound=registered_schema_types[0])
else:
    ConnectionsSchemaList = TypeVar('ConnectionsSchemaList', *registered_schema_types)

class ConnectionSchema(TypingConfig):

    name: str
    type: str
    metadata: dict[str,str] | None
    params: ConnectionsSchemaList
    recon_info: Optional[dict[str,str|int]] = None

    @field_validator('type', mode='after')
    def type_validator(cls, v):

        if v not in connection_types:

            raise ValueError(f'Connection type {v} not registered. The allowed types are {list(connection_types.keys())}')

        return v

class ConnectionsCollectionSchema(TypingConfig):

    sources: list[ConnectionSchema]

    def gather_conn_names(self):

        return {item.name.upper(): item.name for item in self.sources}

class EnvironmentCollectionSchema(TypingConfig):

    environments: dict[EnvironmentCollectionNameEnum, ConnectionsCollectionSchema]

class ConnectionsConfigSchema(TypingConfig):

    connections: EnvironmentCollectionSchema

__all__ = [
    'PostgresConnectionSchema',
    'ConnectionSchema',
    'ConnectionsCollectionSchema',
    'EnvironmentCollectionSchema',
    'ConnectionsConfigSchema',
    'ConnectionTypeEnum',
    'EnvironmentCollectionNameEnum'
    ]