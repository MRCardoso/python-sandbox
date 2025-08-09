import numpy as np
import random
from pysandbox.ecs.component import Component
from pysandbox.helpers import progress_bar, normalize_terrain, normalize_text


class Mask(Component):
    name = "Mask"
    display_name = "Radial Mask"
    strength: float = 2.5
    
    def __init__(self, size, strength=2.5):
        super().__init__(size)
        self.strength = strength
    
    def apply(self, heightmap):
        print('')
        progress_bar(0, prefix=normalize_text(self.display_name, 20))
        cx, cy = self.size // 2, self.size // 2
        X, Y = np.ogrid[:self.size, :self.size]
        dist = np.sqrt((X - cx) **2 + (Y - cy) **2)
        dist = dist / dist.max()
        heightmap *= 1.0 - dist ** self.strength
        progress_bar(100, prefix=normalize_text(self.display_name, 20))
        return heightmap


class River(Component):
    name = "River"
    display_name = "Carve River"
    iterations = 400
    length = 5
    sea_level = 0.4
    def __init__(self, size, iterations = 400, length = 5, sea_level = 0.4):
        super().__init__(size)
        self.iterations = iterations
        self.length = length
        self.sea_level = sea_level

    def apply(self, heightmap):
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

class Erosion(Component):
    # apply simple hydraulic erosion
    name = "Erosion"
    display_name = "Erosion"
    iterations=10000
    strength = 0.01
    def __init__(self, size, iterations=10000, strength=0.01):
        super().__init__(size)
        self.iterations = iterations
        self.strength = strength

    def apply(self, heightmap):
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