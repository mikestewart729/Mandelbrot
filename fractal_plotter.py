# fractal_plotter.py

from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, mandelbrot_smooth, MAX_ITER
from collections import defaultdict
from math import floor, ceil

# Image size (pixels)
WIDTH = 600
HEIGHT = 400

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

# Helper function
def _linear_interpolation(color1, color2, t):
    # The following equation reminds me of homotopy
    return color1 * (1 - t) + color2 * t

def plot_mandelbrot():
    palette = []

    # Initial version, plotting in black and white
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

def plot_mandelbrot_hsv():
    palette = []

    # Initial version, plotting in black and white
    # im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    # Version using hue instead of RGB for color
    im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert x and y pixel coordinates into complex numbers
            z = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            # Compute the escape time
            n = mandelbrot(z)
            # Set the color based on escape time
            # color = 255 - int(n * 255 / MAX_ITER)
            hue = int(255 * n / MAX_ITER)
            saturation = 255
            value = 255 if n < MAX_ITER else 0
            # Plot the point using pillow
            # draw.point([x, y], (color, color, color))
            draw.point([x, y], (hue, saturation, value))

    im.convert('RGB').save('color_output.png', 'PNG')

def plot_mandelbrot_smooth():
    palette = []

    # Plot using HSV for madelbrot smooth
    im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert x and y pixel coordinates into complex numbers
            z = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            # Compute the escape time
            n = mandelbrot_smooth(z)
            # Set the color based on escape time
            hue = int(255 * n / MAX_ITER)
            saturation = 255
            value = 255 if n < MAX_ITER else 0
            # Plot the point using pillow
            draw.point([x, y], (hue, saturation, value))

    im.convert('RGB').save('smooth_output.png', 'PNG')

def plot_mandelbrot_histogram():
    histogram = defaultdict(lambda: 0)
    values = {}
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert x and y pixel coordinates into complex numbers
            z = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            # Compute the number of iterations
            n = mandelbrot_smooth(z)

            values[(x, y)] = n
            if n < MAX_ITER:
                histogram[floor(n)] += 1
    
    total = sum(histogram.values())
    hues = []
    h = 0
    for i in range(MAX_ITER):
        h += histogram[i] / total
        hues.append(h)
    hues.append(h)

    im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            n = values[(x, y)]
            # Color depends on number of iterations
            hue = 255 - int(255 * _linear_interpolation(hues[floor(n)],
                                                        hues[ceil(n)],
                                                        n % 1))
            saturation = 255
            value = 255 if n < MAX_ITER else 0
            # plot the point
            draw.point([x, y], (hue, saturation, value))

    im.convert('RGB').save('histogram_color_output.png', 'PNG')

if __name__ == '__main__':
    plot_mandelbrot_histogram()