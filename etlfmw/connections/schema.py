from pydantic import BaseModel, field_validator
from typing import Optional
from .utils import *


class TypingConfig(BaseModel):

    class Config:
        extra = 'forbid'


@register_schema_type
class PostgresConnectionSchema(TypingConfig):

    host: str
    port: int
    dbname: str
    user: str
    password: str

# Register schema types for each source
allowed_types = None

for type in available_schema_types:

    if allowed_types:

        allowed_types = allowed_types | type
    
    else:

        allowed_types = type

class ConnectionSchema(TypingConfig):

    name: str
    type: str
    metadata: dict[str,str] | None
    params: allowed_types
    recon_info: Optional[dict[str,str|int]] = None

    @field_validator('type', mode='after')
    def type_validator(cls, v):

        if v not in connection_types:

            raise ValueError(f'Connection type {v} not registered. The allowed types are {list(connection_types.keys())}')

        return v

class ConnectionsCollectionSchema(TypingConfig):

    sources: list[ConnectionSchema]

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