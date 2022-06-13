# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks
#
# SPDX-License-Identifier: MIT
"""
Use bitmaptools.rotozoom() to scale a bmp image and show multiple sizes of it on the display.
"""
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

# Create destination Bitmap object to hold the rotated image
dest_bitmap = displayio.Bitmap(
    source_bitmap.height * 2, source_bitmap.height * 2, len(source_palette)
)

# Create a TileGrid to show the destination Bitmap with the rotated image in it
dest_tile_grid = displayio.TileGrid(dest_bitmap, pixel_shader=source_palette)

# rotozoom() takes from source bitmap, puts into destination bitmap.
# clipping is not used so whole source image is put into the destination bitmap.
# scale argument accepts a float number that will multiply the size of the source bitmap times
# the scale factor.

# Big Billie
BIG_BILLIE_SCALE = 1.75
bitmaptools.rotozoom(
    dest_bitmap,
    source_bitmap,
    ox=int(dest_bitmap.width - ((source_bitmap.width / 2) * BIG_BILLIE_SCALE)),
    oy=int((source_bitmap.height / 2) * BIG_BILLIE_SCALE),
    scale=BIG_BILLIE_SCALE,
)

# Normal sized Billie
NORMAL_BILLIE_SCALE = 1.0
bitmaptools.rotozoom(
    dest_bitmap,
    source_bitmap,
    ox=int(dest_bitmap.width / 2) - 24,
    oy=int((source_bitmap.height / 2) * NORMAL_BILLIE_SCALE),
    scale=NORMAL_BILLIE_SCALE,
)

# Little Billie
LITTLE_BILLY_SCALE = 0.5
bitmaptools.rotozoom(
    dest_bitmap,
    source_bitmap,
    ox=int((source_bitmap.width / 2) * LITTLE_BILLY_SCALE),
    oy=int((source_bitmap.height / 2) * LITTLE_BILLY_SCALE),
    scale=LITTLE_BILLY_SCALE,
)

# move the destination image out of the corner a little
dest_tile_grid.x = 10
dest_tile_grid.y = 10

# Create a Group to show the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(dest_tile_grid)

# Add the Group to the Display
display.show(group)

# Loop forever so you can enjoy your image
while True:
    pass
