# -*- coding: utf-8 -*-
from PIL import Image
import subprocess
import ctypes
import os
# Create a 1x1 pixel solid black image
img = Image.new('RGB', (1, 1), color=(0, 0, 0))

# Save the image to the specified path
img.save(r'C:\black_pixel.bmp')

# Path to the image file
image_path = r'C:\black_pixel.bmp'

# The SPI_SETDESKWALLPAPER constant for setting the wallpaper in Windows
SPI_SETDESKWALLPAPER = 20

# Use the ctypes library to call the Windows API to set the wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path , 0)
