from abc import ABC, abstractmethod
from typing import Dict, Union 
from pysandbox.ecs.component import Component

class Entity(ABC):
    _components: Dict[str, Component] = {}    
    def add_component(self, component: Component) -> 'Entity':
        name = component.name.lower()
        if name not in self._components:
            self._components[name] = component
        return self

    def get_component(self, name: str) -> Union[Component, None]:
        name = name.lower()
        if name in self._components:
            return self._components[name]
        return None
    
    @abstractmethod
    def join(self, heightmap):
        pass
    
    @abstractmethod
    def separate(self, heightmap) -> list:
        pass
    
    @abstractmethod
    def generate(self, **kwargs):
        pass