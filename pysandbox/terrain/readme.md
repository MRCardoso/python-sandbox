## Requirements

- numpy
- matplotlib
- noise
- pillow

## Import lib

```python
try:
    sys.path.append("C:\\YourUser\\PATH_TO_PYTHON_SANDBOX")
    from pysandbox.terrain import Terrain, ShapeLayer, RiverCarverLayer, ErosionLayer, SunspotsLayer
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

terrain = Terrain()
heightmap = terrain.run(SIZE, SCALE, OCTAVES, PERSISTENCE, LACUNARITY, SEED, absolute=False)
```

## Add Components

### Radial Shape Layer

```python
terrain.add_component(ShapeLayer(size=SIZE))
```

## Carve River Layer

```python
terrain.add_component(RiverCarverLayer(size=SIZE, iterations=400, length=5, sea_level=0.4))
```

## Erosion Layer

```python
terrain.add_component(ErosionLayer(size=SIZE, iterations=50000))
```

## Sunspots

```python
terrain.add_component(SunspotsLayer(spots=20, radius=30))
```


## Display heightmap combined

Render the heightmap with all layer/component applyed

```python
new_heightmap = terrain.combine(heightmap.copy())
plt.imshow(new_heightmap, cmap="terrain")
plt.title("terrain")
plt.colorbar()
plt.show()
```

## Display heightmap Separated

Render a heightmap for base terrain, and all layer/component applyed  

```python
maps = terrain.separate(heightmap.copy())
map_size = len(maps)
fig, axs = plt.subplots(1, map_size, figsize=(12, 6))
for i in range(map_size):
    label, imap = maps[i]
    axs[i].imshow(imap, cmap='terrain')
    axs[i].set_title(label)
plt.show()
```

## Save Heightmap

```python
new_heightmap = terrain.separate(heightmap.copy())
img = (new_heightmap * 255).astype(np.uint8)
img = Image.fromarray(img)
img.save("terrains/heightmap.jpg")
```

## Load Heightmap

```python
new_heightmap = terrain.separate(heightmap.copy())
img = Image.open("terrains/heightmap.jpg").convert('L').resize((size, size), Image.BICUBIC)
heightmap = np.array(img).astype(np.float32) / 255.0
return heightmap
```