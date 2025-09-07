from abc import ABC, abstractmethod
from typing import Any

class Component(ABC):
    """
    An abstract class for create components in ECS system
    
    Attributes
    ----------
    display_name (str)
        The displayed Name of Layer
    size (int)
        The size of the heightmap 
    """
    display_name = 'Default'
    size: int

    def __init__(self: 'Component', size: int) -> None:
        self.size = size

    @property
    def name(self):
        return self.display_name.replace(" ", "_").lower().strip()
    
    @abstractmethod
    def apply(self, data: Any):
        pass