from abc import ABC, abstractmethod
from typing import Dict, Union, Any
from pysandbox.ecs.component import Component

class Entity(ABC):
    """
    An abstract class for create entity in ECS system
    
    Attributes
    ----------
    _components (Dict[str, Component])
        The list of components plugged in to run modifiers on abstract methods
    """
    _components: Dict[str, Component] = {} 

    def add_component(self: "Entity", component: Component) -> 'Entity':
        if component.name not in self._components:
            self._components[component.name] = component
        return self

    def get_component(self: "Entity", name: str) -> Union[Component, None]:
        name = name.lower().strip()
        if name in self._components:
            return self._components[name]
        return None
    
    def combine(self: "Entity", data: Any):
        for _, component in self._components.items():
            data = component.apply(data)
        return data
    
    @abstractmethod
    def run(self: "Entity", **kwargs):
        pass