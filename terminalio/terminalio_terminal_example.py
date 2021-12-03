# SPDX-FileCopyrightText: Copyright (c) 2021 Randall Bohn (dexter)
#
# SPDX-License-Identifier: MIT
"""
Demonstrate usage of the terminalio module.

The module provides a VT100 emulation within a displayo.TileGrid.
A good reference for VT100 "escape" codes is found at
https://www.csie.ntu.edu.tw/~r92094/c++/VT100.html
"""
import random
import time
import board
import displayio
import terminalio

display = board.DISPLAY
group = displayio.Group()
display.show(group)

palette = displayio.Palette(2)
palette[0] = 0x220000
palette[1] = 0x00FFFF

ROWS = 12
COLS = 40

w, h = terminalio.FONT.get_bounding_box()

termgrid = displayio.TileGrid(
    terminalio.FONT.bitmap,
    pixel_shader=palette,
    y=20,
    width=COLS,
    height=ROWS,
    tile_width=w,
    tile_height=h,
)
group.append(termgrid)
term = terminalio.Terminal(termgrid, terminalio.FONT)


def world_seed(n):
    """For entertainment purposes only."""
    letters = "AEIOUMRFCV"
    word = [random.choice(letters) for _ in range(n)]
    return "".join(word)


term.write("Terminal %dx%d:\r\n" % (COLS, ROWS))
term.write("  %dx%d pixels.\r\n" % (COLS * w, ROWS * h))
term.write("VT100 protocol.\r\n")
term.write("Both carriage return and line feed are required.\r\n")
while True:
    term.write("Your world seed is:\r\n")
    for _ in range(10):
        term.write(world_seed(12) + " ")
    term.write("\r\n")
    time.sleep(10)
