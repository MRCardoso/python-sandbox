import sys

def progress_bar(percentage):
        bar_length = 50
        filled_length = int(bar_length * percentage / 100)
        bar = '=' * filled_length + '-' * (bar_length - filled_length)
        sys.stdout.write(f'\r[{bar}] {percentage:.2f}%')
        sys.stdout.flush()

def normalize_terrain(terrain):
    return (terrain - terrain.min()) / (terrain.max() - terrain.min())