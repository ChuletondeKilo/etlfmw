from typing import Any
from ..interfaces import ExtractorI, ConnectionI as ExtractorI, ConnectionI
from ..loggers import log_message
from ..config.schema import ExtractorSchema

class Extractor(ExtractorI):

    def __init__(self, connection: ConnectionI, extractor_schema: ExtractorSchema):
        self.extractor_schema = extractor_schema
        self.connection = connection

    def extract(self, **kwargs) -> Any:
        
        log_message('execution_logs', '1234')
        self.connection.connect()
        result = self.connection.execute(**kwargs)
        self.connection.disconnect()

        return result

__all__ = ['Extractor']