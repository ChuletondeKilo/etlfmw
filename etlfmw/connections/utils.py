from enum import Enum
from pydantic import BaseModel
from typing import Type

connection_types = {}

def register_connection_class(name: str):

    def decorator(cls):

        def wrapper(*args, **kwargs):

            return cls(*args, **kwargs)
        
        global connection_types

        connection_types[name] = cls

        return wrapper

    return decorator

# Registry to store models
registered_schema_types: list[Type[BaseModel]] = []

def register_connection_type(cls: Type[BaseModel]) -> Type[BaseModel]:
    registered_schema_types.append(cls)
    return cls

class EnvironmentCollectionNameEnum(Enum):

    LOCAL = 'local'
    DEV = 'dev'
    TEST = 'test'
    PROD = 'prod'