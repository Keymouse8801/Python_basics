import math
from math import pi

figure_type = str(input())

if figure_type == "square":
    side_a = float(input())
    volume = side_a * side_a
    print(f'{volume:.3f}')
elif figure_type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    volume = side_a * side_b
    print(f'{volume:.3f}')
elif figure_type == "circle":
    side_a = float(input())
    volume = pi * (side_a * side_a)
    print(f'{volume:.3f}')
elif figure_type == "triangle":
    side_a = float(input())
    side_b = float(input())
    volume = (side_a * side_b) / 2
    print(f'{volume:.3f}')

