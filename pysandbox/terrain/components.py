import numpy as np
from numpy.typing import NDArray
import random
from pysandbox.ecs.component import Component
from pysandbox.helpers import progress_bar, normalize_terrain, normalize_text

class ShapeLayer(Component):
    """
    Radial falloff mask that shapes the terrain into island or continent-like

    structures by lowering elevation near the map edges.
    
    Attributes
    ----------
    display_name (str)
        The Displayed Name of Layer
    strength (float)
        The pow to increase in heightmap
    """
    display_name = "Radial Mask"
    strength: float = 2.5
    
    def __init__(self: "ShapeLayer", size: int, strength=2.5):
        super().__init__(size)
        self.strength = strength
    
    def apply(self: "ShapeLayer", heightmap: NDArray[np.float32]) -> NDArray[np.float32]:
        print('')
        progress_bar(0, prefix=normalize_text(self.display_name, 20))
        cx, cy = self.size // 2, self.size // 2
        X, Y = np.ogrid[:self.size, :self.size]
        dist = np.sqrt((X - cx) **2 + (Y - cy) **2)
        dist = dist / dist.max()
        heightmap *= 1.0 - dist ** self.strength
        progress_bar(100, prefix=normalize_text(self.display_name, 20))
        return heightmap


class RiverCarverLayer(Component):
    """
    Carves downhill paths into the terrain to simulate rivers.

    Starting points are chosen randomly, and elevation is lowered

    along the steepest descent to create flowing channels.
    
    Attributes
    ----------
    display_name (str)
        The Displayed Name of Layer
    iterations (int)
        Amount of iterations over each length
    length (int)
        Amount of iterations in heightmap    
    sea_level (float)
        The sea level boundary
    """
    display_name = "River Carver"
    iterations = 400
    length = 5
    sea_level = 0.4

    def __init__(self: "RiverCarverLayer", size: int, iterations = 400, length = 5, sea_level = 0.4):
        super().__init__(size)
        self.iterations = iterations
        self.length = length
        self.sea_level = sea_level

    def apply(self: "RiverCarverLayer", heightmap: NDArray[np.float32]) -> NDArray[np.float32]:
        print('')
        if not self.iterations or not self.length:
            raise Exception("The amount of length or iterations can't be zero")
        for it in range(self.length):
            x, y = (
                np.random.randint(int(self.iterations/4), self.iterations),
                np.random.randint(int(self.iterations/4), self.iterations)
            )
            progress_bar(((it + 1) / self.length) * 100, prefix=normalize_text(self.display_name, 20))
            for _ in range(self.iterations):
                if heightmap[x, y] <= self.sea_level:
                    break
                heightmap[x, y] -= 0.03
                neighbors = [
                    (x+i, y+j)
                    for i in [-1,0,1] 
                    for j in [-1,0,1]
                    if 0 <= x+i < self.size and 0 <= y+j < self.size
                ]
                if random.random() < 0.15:
                    random.shuffle(neighbors)
                x, y = min(neighbors, key=lambda p: heightmap[p[0], p[1]])
        # Normalize
        return normalize_terrain(heightmap)

class ErosionLayer(Component):
    """
    Applies a simple hydraulic erosion simulation.

    Random raindrops are placed on the terrain,
    
    carrying sediment downhill and depositing it in lower regions, 
    
    producing smoother and more natural landforms.
    
    Attributes
    ----------
    display_name (str)
        The Displayed Name of Layer
    iterations (int)
        Amount of iterations on heightmap
    strength (float)
        The drops strength for each iteration 
    """
    display_name = "Erosion"
    iterations = 10000
    strength = 0.01

    def __init__(self: "ErosionLayer", size: int, iterations = 10000, strength = 0.01):
        super().__init__(size)
        self.iterations = iterations
        self.strength = strength

    def apply(self: "ErosionLayer", heightmap: NDArray[np.float32]) -> NDArray[np.float32]:
        print('')
        for it in range(self.iterations):
            progress_bar(((it + 1) / self.iterations) * 100, prefix=normalize_text(self.display_name, 20))
            x = np.random.randint(1, self.size - 1)
            y = np.random.randint(1, self.size - 1)
            h = heightmap[x, y]
            dx, dy = 0, 0
            min_h = h
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if heightmap[x + i, y + j] < min_h:
                        min_h = heightmap[x + i, y + j]
                        dx, dy = i, j
            
            # erode if we have a slope
            if dx != 0 or dy != 0:
                drop = (h - min_h) * self.strength
                heightmap[x, y] -= drop
                heightmap[x + dx, y + dy] += drop # sediment deposition
            
        # Normalize again
        return normalize_terrain(heightmap)

class SunspotsLayer(Component):
    """
    Applies sunspots to heightmap

    Attributes
    ----------
    display_name (str)
        The Displayed Name of Layer
    spots (int)
        Amount of spots on heightmap
    radius (int)
        the maximum radius 
    """
    display_name = "Sunspots"
    spots = 20
    radius = 30

    def __init__(self: "SunspotsLayer", size, spots = 20, radius = 30):
        super().__init__(size)
        self.spots = spots
        self.radius = radius

    def apply(self: "SunspotsLayer", heightmap: NDArray[np.float32]) -> NDArray[np.float32]:
        print('')
        size = heightmap.shape[0]
        
        for it in range(self.spots):
            progress_bar(((it + 1) / self.spots) * 100, prefix=normalize_text(self.display_name, 20))
            cx, cy = np.random.randint(0, size), np.random.randint(0, size)
            r = np.random.randint(2, self.radius)
            
            Y, X = np.ogrid[:size, :size]
            dist = np.sqrt((X - cx)**2 + (Y - cy)**2)
            mask = np.clip(1 - (dist / r), 0, 1)
            heightmap *= (1 - mask * np.random.uniform(0.6, 0.9))
        return heightmap
        