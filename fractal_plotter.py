# fractal_plotter.py

from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, MAX_ITER

# Image size (pixels)
WIDTH = 600
HEIGHT = 400

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

palette = []

im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # Convert x and y pixel coordinates into complex numbers
        z = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # Compute the escape time
        n = mandelbrot(z)
        # Set the color based on escape time
        color = 255 - int(n * 255 / MAX_ITER)
        # Plot the point using pillow
        draw.point([x, y], (color, color, color))

im.save('output.png', 'PNG')
