import board
import displayio
"""
Illustrate usage of displayio.Shape with boundary and mirror.
"""

SHAPE_WIDTH = board.DISPLAY.width
SHAPE_HEIGHT = board.DISPLAY.height
CORNER_SIZE = board.DISPLAY.width // 4
display = board.DISPLAY

shape = displayio.Shape(SHAPE_WIDTH, SHAPE_HEIGHT, mirror_x=True, mirror_y=True)

palette = displayio.Palette(2)

# set corner pixels out of bounds
for i in range(CORNER_SIZE):
    shape.set_boundary(i, CORNER_SIZE-1-i, SHAPE_WIDTH//2-1)

palette[0] = 0x0000FF  # out of bounds color
palette[1] = 0x00FFFF  # shape color

tile_grid = displayio.TileGrid(shape, pixel_shader=palette)
group = displayio.Group()
group.append(tile_grid)
display.show(group)

# loop forever to keep it on the screen
while True:
    pass
