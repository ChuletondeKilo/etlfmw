from pydantic import BaseModel
from ..connections.main import available_connections

class TypingConfig(BaseModel):

    class Config:
        extra = 'forbid'

class ExtractorSchema(TypingConfig):

    name: str
    source: available_connections
    query: str

class ExtractorCollectionSchema(TypingConfig):

    extract: list[ExtractorSchema]

class LoaderSchema(TypingConfig):

    name: str
    loader: str

class LoaderCollectionSchema(TypingConfig):

    load: list[LoaderSchema]

class PipelineSchema(TypingConfig):

    name: str
    metadata: dict[str, str | int]
    steps: dict[str, list[ExtractorSchema | LoaderSchema] | ExtractorSchema | LoaderSchema] | None

class PipelineCollectionSchema(TypingConfig):

    pipelines: list[PipelineSchema]

class PipelinesConfigSchema(TypingConfig):

    config: PipelineCollectionSchema

    def pipelines_list(self) -> list[PipelineSchema]:

        return self.config.pipelines

__all__ = [
    'PipelinesConfigSchema',
    'PipelineSchema',
    'PipelineCollectionSchema',
    'ExtractorSchema',
    'ExtractorCollectionSchema',
    'LoaderSchema',
    'LoaderCollectionSchema'
    ]