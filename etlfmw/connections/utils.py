from enum import Enum
from pydantic import BaseModel
from typing import Type, TypeVar

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
available_schema_types = []

def register_schema_type(cls):

    def wrapper(*args, **kwargs):

        return cls(*args, **kwargs)
    
    global available_schema_types

    available_schema_types.append(cls)

    return wrapper


class EnvironmentCollectionNameEnum(Enum):

    LOCAL = 'local'
    DEV = 'dev'
    TEST = 'test'
    PROD = 'prod'