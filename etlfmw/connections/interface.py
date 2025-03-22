from abc import ABC, abstractmethod

class ConnectionI(ABC):
    @abstractmethod
    def connect(self): ...

    @abstractmethod
    def disconnect(self): ...

    @abstractmethod
    def reconnect(self): ...

    @abstractmethod
    def execute(self, query): ...

    @abstractmethod
    def load(self, data): ...
