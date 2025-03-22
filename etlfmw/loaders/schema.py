from pydantic import BaseModel

class TypingConfig(BaseModel):

    class Config:
        extra = 'forbid'

class LoaderSchema(TypingConfig):

    name: str
    loader: str

class LoaderCollectionSchema(TypingConfig):

    load: list[LoaderSchema]
