# SPDX-FileCopyrightText: 2022 David Glaude (based on 2021 ladyada for Adafruit Industries)
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, and some white text.
Customized version of displayio_ssd1306_simpletest.py for 64x32
"""

import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=64, height=32)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(64, 32, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

## Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(62, 30, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black

inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=1, y=1)
splash.append(inner_sprite)

text = "Hello"
text_area = label.Label( terminalio.FONT, text=text, color=0xFFFFFF, x=2, y=6)
splash.append(text_area)

text = "World"
text_area = label.Label( terminalio.FONT, text=text, color=0xFFFFFF, x=32, y=15)
splash.append(text_area)

text = "9876543210"
text_area = label.Label( terminalio.FONT, text=text, color=0xFFFFFF, x=2, y=24)
splash.append(text_area)

while True:
    pass
