from typing import Any
from ..interfaces import LoaderI, ConnectionI as LoaderI, ConnectionI

class Loader(LoaderI):

    def __init__(self, config: Any, connection: ConnectionI):
        self.config = config or None
        self.connection = connection

    def load(self) -> Any:
        
        self.connection.connect()
        result = self.connection.execute()
        self.connection.disconnect()

        return result