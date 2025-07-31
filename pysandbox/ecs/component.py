from abc import ABC, abstractmethod

class Component(ABC):
    name: str = 'Default'
    display_name = 'Default'
    planet_name: str = 'none'
    size: int
    def __init__(self, planet_name, size):
        self.planet_name = planet_name
        self.size = size
    
    @abstractmethod
    def apply(self, heightmap):
        pass