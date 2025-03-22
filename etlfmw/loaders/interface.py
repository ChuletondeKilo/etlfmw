from abc import ABC, abstractmethod
from ..connections.base import Connection

class LoaderI(ABC):
    @abstractmethod
    def extract(self, connection: Connection): ...