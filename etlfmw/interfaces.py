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

class ExtractorI(ABC):
    @abstractmethod
    def extract(self, connection: ConnectionI): ...

class LoaderI(ABC):
    @abstractmethod
    def load(self, connection: ConnectionI, data): ...

class PipelineI(ABC):
    @abstractmethod
    def run(self): ...