from typing import Any
from ...interfaces import LoaderI, ConnectionI as LoaderI, ConnectionI
from ..schema import LoaderSchema
from uuid import uuid4

class Loader(LoaderI):

    def __init__(self, config: Any, connection: ConnectionI, loader_schema: LoaderSchema):

        self.loader_uuid = uuid4()
        self.loader_schema = loader_schema
        self.connection = connection

    def load(self) -> Any:
        
        self.connection.connect()
        result = self.connection.execute()
        self.connection.disconnect()

        return result