"""
Illustrate usage of displayio.Shape.
"""

import board
import displayio

SHAPE_WIDTH = 100
SHAPE_HEIGHT = 100
display = board.DISPLAY

shape = displayio.Shape(SHAPE_WIDTH, SHAPE_HEIGHT, mirror_x=False, mirror_y=False)

palette = displayio.Palette(2)

palette[1] = 0x00FFFF  # shape color

tile_grid = displayio.TileGrid(shape, pixel_shader=palette)
group = displayio.Group()
group.append(tile_grid)
display.show(group)

while True:
    pass
