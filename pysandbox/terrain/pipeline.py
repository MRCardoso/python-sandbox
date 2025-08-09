import os
import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from noise import pnoise2
from PIL import Image
from pysandbox.helpers import progress_bar, normalize_terrain, normalize_text
from pysandbox.ecs.entity import Entity


class Terrain(Entity):
    # 1. Generate Perlin Noise Terrain
    heightmap = None
    def generate(self, size: int, scale: float, octaves: float, persistence: float, lacunarity: float, seed: float, absolute=False) -> NDArray[np.float64]:
        print('')
        terrain = np.zeros((size, size), dtype=np.float32)
        for x in range(size):
            progress_bar(((x + 1) / size) * 100, normalize_text(f"Generate Terrain", 20))
            for y in range(size):
                nx = x / scale
                ny = y / scale
                value = pnoise2(
                    nx,
                    ny,
                    octaves=octaves,
                    persistence=persistence,
                    lacunarity=lacunarity,
                    repeatx=size,
                    repeaty=size,
                    base=seed
                )
                terrain[x][y] = abs(value) if absolute else value
        # normalize
        return normalize_terrain(terrain)
    
    def join(self, heightmap):
        for _, component in self._components.items():
            heightmap = component.apply(heightmap)
        return heightmap
    
    def separate(self, heightmap):
        return [('Original', heightmap)] + [
            (component.display_name, component.apply(heightmap.copy())) 
            for _, component in self._components.items()
        ]

class Heightmap:
    @staticmethod
    def save(heightmap, base_path, filename='heightmap.jpg'):
        print("\nSaving heighmap")
        img = (heightmap * 255).astype(np.uint8)
        img = Image.fromarray(img)
        if not os.path.isdir(base_path):
            os.mkdir(base_path)
        img.save(f'{base_path}/{filename}')
    
    @staticmethod
    def display(maps: list):
        map_size = len(maps)
        if map_size == 1:
            label, imap = maps[0]
            plt.imshow(imap, cmap='terrain')
            plt.title(label)
            plt.colorbar()
            plt.show()
            return
        # 3. Display result
        fig, axs = plt.subplots(1, map_size, figsize=(12, 6))
        for i in range(map_size):
            label, imap = maps[i]
            axs[i].imshow(imap, cmap='terrain')
            axs[i].set_title(label)
        plt.show()