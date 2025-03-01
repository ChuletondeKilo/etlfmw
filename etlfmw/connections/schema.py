from pydantic import BaseModel
from typing import Union, List, Dict, Optional
from enum import Enum

class EnvironmentCollectionNameEnum(Enum):

    LOCAL = 'local'
    DEV = 'dev'
    TEST = 'test'
    PROD = 'prod'

class TypingConfig(BaseModel):

    class Config:
        extra = 'forbid'

class PostgresConnectionSchema(TypingConfig):

    host: str
    port: int
    dbname: str
    user: str
    password: str

class ConnectionSchema(TypingConfig):

    name: str
    type: str
    metadata: Optional[Dict[str,str]]
    params: Union[PostgresConnectionSchema]

class ConnectionsCollectionSchema(TypingConfig):

    connections: List[ConnectionSchema]

class EnvironmentCollectionSchema(TypingConfig):

    environments: Dict[EnvironmentCollectionNameEnum, ConnectionsCollectionSchema]

class ConnectionsConfigSchema(TypingConfig):

    connections: EnvironmentCollectionSchema