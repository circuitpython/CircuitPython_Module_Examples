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
INITIAL_SCALE = 0.5
bitmaptools.rotozoom(dest_bitmap, source_bitmap, scale=INITIAL_SCALE)

# move the destination image out of the corner a little
dest_tile_grid.x = 10
dest_tile_grid.y = 10

# Create a Group to show the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(dest_tile_grid)

# Add the Group to the Display
display.show(group)

# we will manually refresh the display only after we make changes to our destination bitmap
display.auto_refresh = False

# Loop forever
while True:
    # loop from 0.5 to 2.0 scale factors. step size 0.1
    for scale in range(5, 21):
        # empty the destination bitmap, clear out the previously drawn frame
        dest_bitmap.fill(0)

        # paste in billie at the current scale size from our loop
        bitmaptools.rotozoom(dest_bitmap, source_bitmap, scale=scale / 10)

        # refresh the display to draw our changes
        display.refresh()

    # loop from 2.0 to 0.5 scale factors. step size 0.1
    for scale in range(20, 4, -1):
        # empty the destination bitmap, clear out the previously drawn frame
        dest_bitmap.fill(0)

        # paste in billie at the current scale size from our loop
        bitmaptools.rotozoom(dest_bitmap, source_bitmap, scale=scale / 10)

        # refresh the display to draw our changes
        display.refresh()
