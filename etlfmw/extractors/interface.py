from abc import ABC, abstractmethod
from ..connections.base import Connection

class ExtractorI(ABC):
    @abstractmethod
    def extract(self, connection: Connection): ...