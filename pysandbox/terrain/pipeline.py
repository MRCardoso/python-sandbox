import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from noise import pnoise2
from PIL import Image
from pysandbox.helpers import progress_bar, normalize_terrain, normalize_text
from pysandbox.ecs.entity import Entity


class Terrain(Entity):
    """
    Base terrain entity that generates the initial heightmap for a planet.

    This class provides the starting elevation field using procedural noise
    (Perlin, fractal, or custom). 
    
    It acts as the foundation on which additional
    layers (e.g., ShapeLayer, RiverCarverLayer, ErosionLayer) 
    are applied to shape the final terrain.
    
    """
    
    def run(self: "Terrain", size: int, scale: float, octaves: float, persistence: float, lacunarity: float, seed: float, absolute=False) -> NDArray[np.float32]:
        """
        Creates the base heightmap using noise and normalizes it to [0, 1].
        
        Parameters
        ----------
        
        size (int): 
            Resolution of the heightmap (width x height).
        scale (float):
            Noise scaling factor, controlling zoom of terrain features.
        octaves (float):
            Number of noise octaves for fractal detail.
        persistence (float): 
            Amplitude decay across octaves (lower = smoother).
        lacunarity (float):
            Frequency growth across octaves (higher = sharper).
        seed (float):
            Random seed for deterministic generation.
        absolute (bool):
            When True use abs to generated noise
        
        Returns
        -------
        heightmap (NDArray[np.float32])
            2D array of normalized float values (0.0-1.0)
        """
        print('')
        custom_args = {"octaves": octaves, "persistence": persistence, "lacunarity": lacunarity}
        custom_args = {x: custom_args[x] for x in custom_args if custom_args[x] > 0}
        terrain = np.zeros((size, size), dtype=np.float32)
        for x in range(size):
            progress_bar(((x + 1) / size) * 100, normalize_text(f"Generate Terrain", 20))
            for y in range(size):
                nx = x / scale
                ny = y / scale
                value = pnoise2(
                    nx,
                    ny,
                    **custom_args,
                    repeatx=size,
                    repeaty=size,
                    base=seed
                )
                terrain[x][y] = abs(value) if absolute else value
        # normalize
        return normalize_terrain(terrain)
    
    def separate(self: "Terrain", heightmap):
        return [('Original', heightmap)] + [
            (component.display_name, component.apply(heightmap.copy())) 
            for _, component in self._components.items()
        ]