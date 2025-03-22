from abc import ABC, abstractmethod
from ..extractors.base import Extractor
from ..loaders.base import Loader

class PipelineI(ABC):
    @abstractmethod
    def run(self): ...