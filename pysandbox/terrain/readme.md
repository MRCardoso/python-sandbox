# Usage


## Import lib

```python
try:
    sys.path.append("C:\\YourUser\\PATH_TO_PYTHON_SANDBOX")
    from pysandbox.terrain.pipeline import Terrain, Heightmap
    from pysandbox.terrain.components import Erosion, Mask, River
except:
    print("Fail To load python-sandbox")
    exit()
```

## Generate Heightmap

```python
SIZE = 512
SCALE = 80
OCTAVES = 5
PERSISTENCE = 0.5
LACUNARITY = 2.0
SEED = np.random.randint(0,100)
terrain_name = "randon"

terrain = Terrain()
heightmap = terrain.generate(terrain_name, SIZE, SCALE, OCTAVES, PERSISTENCE, LACUNARITY, SEED, absolute=False)
```

## Add Components

### Mask

```python
terrain.add_component(Mask(planet_name=terrain_name, size=SIZE))
```

## River

```python
terrain.add_component(River(planet_name=terrain_name, size=SIZE, iterations=400, length=5))
```

## Erosion

```python
terrain.add_component(Erosion(planet_name=terrain_name, size=SIZE, iterations=50000))
```


## Display heightmap joined


```python
new_heightmap = terrain.join(heightmap.copy())
Heightmap.display([(terrain_name, new_heightmap)])
```

## Display heightmap Separated

```python
new_heightmap = terrain.separate(heightmap.copy())
Heightmap.display(new_heightmap)
```


## Save Heightmap

```python
new_heightmap = terrain.separate(heightmap.copy())
Heightmap.save(new_heightmap, f"terrains/{terrain_name}", "heightmap.jpg")
```