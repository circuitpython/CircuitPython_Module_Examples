import board
import displayio

display = board.DISPLAY

# Create a bitmap with two colors
bitmap = displayio.Bitmap(display.width, display.height, 2)

# Create a two color palette
palette = displayio.Palette(2)

palette[0] = 0xBB33BB  # screen color

# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Create a Group
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.show(group)

# Loop forever so you can enjoy your image
while True:
    pass
