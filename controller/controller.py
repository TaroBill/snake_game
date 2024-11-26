from snake import Direction
from abc import ABC, abstractmethod

class IController(ABC):
    @abstractmethod
    def get_Direction(self) -> Direction:
        pass
    @abstractmethod
    def start_button(self) -> bool:
        pass