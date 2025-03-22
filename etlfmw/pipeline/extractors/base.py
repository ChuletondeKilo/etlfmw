from typing import Any
from ...interfaces import ExtractorI, ConnectionI as ExtractorI, ConnectionI
from ..schema import ExtractorSchema
from uuid import uuid4

class Extractor(ExtractorI):

    def __init__(self, connection: ConnectionI, extractor_schema: ExtractorSchema):

        self.extractor_uuid = uuid4()
        self.extractor_schema = extractor_schema
        self.connection = connection

    def extract(self, **kwargs) -> Any:
        
        print('execution_logs', self.extractor_uuid)
        self.connection.connect()
        result = self.connection.execute(**kwargs)
        self.connection.disconnect()

        return result

__all__ = ['Extractor']