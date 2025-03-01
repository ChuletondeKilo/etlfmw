from pydantic import BaseModel
from typing import Union, List, Dict, Optional

class TypingConfig(BaseModel):

    class Config:
        extra = 'forbid'

class ExtractorSchema(TypingConfig):

    name: str
    query: str

class ExtractorCollectionSchema(TypingConfig):

    extract: List[ExtractorSchema]

class LoaderSchema(TypingConfig):

    name: str
    loader: str

class LoaderCollectionSchema(TypingConfig):

    load: List[LoaderSchema]

class PipelineSchema(TypingConfig):

    name: str
    metadata: Dict[str, Union[str,int]]
    steps: Dict[str, Optional[Union[List[Union[ExtractorSchema, LoaderSchema]], ExtractorSchema, LoaderSchema]]]

class PipelineCollectionSchema(TypingConfig):

    pipelines: List[PipelineSchema]

class PipelinesConfigSchema(TypingConfig):

    config: PipelineCollectionSchema

__all__ = [
    'PipelinesConfigSchema',
    'PipelineSchema',
    'PipelineCollectionSchema',
    'ExtractorSchema',
    'ExtractorCollectionSchema',
    'LoaderSchema',
    'LoaderCollectionSchema'
    ]