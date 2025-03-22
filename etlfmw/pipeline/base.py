from .schema import PipelinesConfigSchema
from ..interfaces import PipelineI
import extractors.base
import loaders.base
from .config import config as pipeline_schema
from uuid import uuid4

class Pipeline(PipelineI):

    def __init__(self, config: PipelinesConfigSchema):

        self.pipeline_uuid = uuid4()
        self.pipeline_schema = pipeline_schema

    def get_pipeline(self, pipeline_name: str) -> PipelineConfig:

        return PipelineConfig(self.config[pipeline_name])