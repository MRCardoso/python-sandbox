import sys

def progress_bar(percentage: float, prefix=''):
    bar_length = 50
    filled_length = int(bar_length * percentage / 100)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\r{prefix}[{bar}] {percentage:.2f}%')
    sys.stdout.flush()

def normalize_terrain(terrain):
    return (terrain - terrain.min()) / (terrain.max() - terrain.min())

def normalize_text(value: str, size=10):
    return f'{value:>{size}}'