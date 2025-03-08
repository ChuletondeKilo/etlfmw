from pydantic import BaseModel
from typing import Type, TypeVar, Optional
from enum import Enum

# Registry to store models
registered_types: list[Type[BaseModel]] = []

def register_connection_type(cls: Type[BaseModel]) -> Type[BaseModel]:
    registered_types.append(cls)
    return cls


class ConnectionTypeEnum(Enum):

    POSTGRES = 'postgres'

class EnvironmentCollectionNameEnum(Enum):

    LOCAL = 'local'
    DEV = 'dev'
    TEST = 'test'
    PROD = 'prod'

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

if len(registered_types) == 1:
    ConnectionsSchemaList = TypeVar('ConnectionsSchemaList', bound=registered_types[0])
else:
    ConnectionsSchemaList = TypeVar('ConnectionsSchemaList', *registered_types)

class ConnectionSchema(TypingConfig):

    name: str
    type: ConnectionTypeEnum
    metadata: dict[str,str] | None
    params: ConnectionsSchemaList
    recon_info: Optional[dict[str,str|int]] | None = None

class ConnectionsCollectionSchema(TypingConfig):

    sources: list[ConnectionSchema]

    def gather_conn_names(self):

        return {item.name.upper(): item.name for item in self.sources}

class EnvironmentCollectionSchema(TypingConfig):

    environments: dict[EnvironmentCollectionNameEnum, ConnectionsCollectionSchema]

class ConnectionsConfigSchema(TypingConfig):

    connections: EnvironmentCollectionSchema

    def instantiate_connections(self):

        ...

__all__ = [
    'PostgresConnectionSchema',
    'ConnectionSchema',
    'ConnectionsCollectionSchema',
    'EnvironmentCollectionSchema',
    'ConnectionsConfigSchema',
    'ConnectionTypeEnum',
    'EnvironmentCollectionNameEnum'
    ]