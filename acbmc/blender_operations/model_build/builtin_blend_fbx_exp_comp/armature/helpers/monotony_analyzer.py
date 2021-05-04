from abc import ABC, abstractmethod
from typing import Any, List

class MonotonyAnalyzer(ABC):
    def __init__(self):
        self.elements = []  # type: List[Any]

    def consider(self, element: Any):
        self.elements.append(element)

    @abstractmethod
    def raise_exception_if_monotonous(self):
        raise NotImplementedError
