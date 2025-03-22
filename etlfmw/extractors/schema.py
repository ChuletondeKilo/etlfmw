from pydantic import BaseModel, field_validator
from ..connections.utils import connection_types

class TypingConfig(BaseModel):

    class Config:
        extra = 'forbid'

class ExtractorSchema(TypingConfig):

    name: str
    type: str
    query: str

    @field_validator('type', mode='after')
    def type_validator(cls, v):

        if v not in connection_types:

            raise ValueError(f'Connection type {v} not registered. The allowed types are {list(connection_types.keys())}')

        return v

class ExtractorCollectionSchema(TypingConfig):

    extract: list[ExtractorSchema]