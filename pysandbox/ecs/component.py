from abc import ABC, abstractmethod

class Component(ABC):
    name: str = 'Default'
    display_name = 'Default'
    size: int
    def __init__(self, size):
        self.size = size
    
    @abstractmethod
    def apply(self, heightmap):
        pass