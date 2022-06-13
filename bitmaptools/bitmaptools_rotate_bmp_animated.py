# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks
#
# SPDX-License-Identifier: MIT
"""
Use bitmaptools.rotozoom() to rotate a bmp image in a circle animated.
"""
import math
import board
import adafruit_imageload
import bitmaptools
import displayio

# use the builtin display
display = board.DISPLAY

# load bmp image into a Bitmap and Palette objects
source_bitmap, source_palette = adafruit_imageload.load(
    "Billie.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette
)
# Create a TileGrid to show the bitmap
source_tile_grid = displayio.TileGrid(source_bitmap, pixel_shader=source_palette)

# Create destination Bitmap object to hold the rotated image
dest_bitmap = displayio.Bitmap(
    source_bitmap.height, source_bitmap.height, len(source_palette)
)

# Create a TileGrid to show the destination Bitmap with the rotated image in it
dest_tile_grid = displayio.TileGrid(dest_bitmap, pixel_shader=source_palette)

# move the rotated image tilegrid over to the right some
dest_tile_grid.x = 100

# Create a Group to show the TileGrids
group = displayio.Group()

# Add the TileGrids to the Group
group.append(source_tile_grid)
group.append(dest_tile_grid)

# Add the Group to the Display
display.show(group)

# Loop forever so you can enjoy your image
while True:
    # loop over all the degrees from 0-360
    for angle_deg in range(360):
        # erase previous frame
        dest_bitmap.fill(0)

        # take from source bitmap, put into destination bitmap.
        # default values for x,y locations and clipping so whole image is used
        # angle argument accepts radians. You can use math module to convert from degrees
        bitmaptools.rotozoom(dest_bitmap, source_bitmap, angle=math.radians(angle_deg))
