import random
from turtle import *

# Setup window and coordinates
setup(600, 600)
setworldcoordinates(-6, -1, 5, 11)
tracer(0)  # Disable auto-updating for speed
bgcolor("black")
up()  # Lift pen (we’ll use dots instead of drawing lines)

# Starting point
p = (0, 0)

# Main loop: draw 100,000 points
for i in range(100000):
    goto(p)
    dot(2, "#00AF00")  # Draw small green dot

    # Randomly choose a transformation
    r = random.random()
    if r < 0.01:  # Stem
        p = (0, 0.16 * p[1])
    elif r < 0.86:  # Main fern body
        p = (0.85 * p[0] - 0.04 * p[1], -0.04 * p[0] + 0.85 * p[1] + 1.6)
    elif r < 0.93:  # Left leaflet
        p = (0.2 * p[0] - 0.26 * p[1], -0.23 * p[0] + 0.22 * p[1] + 1.6)
    else:  # Right leaflet
        p = (-0.15 * p[0] + 0.28 * p[1], 0.26 * p[0] + 0.24 * p[1] + 0.44)

    # Update the screen every 1000 iterations
    if i % 1000 == 0:
        update()

done()
