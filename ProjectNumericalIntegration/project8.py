#Joshua Simpson
#CST 305
#4/28/2024
#This Python script calculates and visualizes the left,
#right, and midpoint Riemann sums for numerical integration
#of different mathematical functions over specified intervals.

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

matplotlib.use('TkAgg')  # Set the backend for matplotlib

# Part 1: Implementing Riemann Sums for Numerical Integration

def compute_riemann_sum(lower_limit, upper_limit, integrand, intervals, part_title):
    computation_start = time.time()
    marker_size = 0 if intervals > 50 else 5
    dx = (upper_limit - lower_limit) / intervals
    x_values = np.linspace(lower_limit, upper_limit, intervals + 1)
    y_values = integrand(x_values)

    # Left Riemann Sum
    left_x = x_values[:-1]
    left_heights = y_values[:-1]
    left_area = np.sum(dx * left_heights)
    print(f'{part_title}: Left Riemann Approx. Area = {left_area}')

    # Right Riemann Sum
    right_x = x_values[1:]
    right_heights = y_values[1:]
    right_area = np.sum(dx * right_heights)
    print(f'{part_title}: Right Riemann Approx. Area = {right_area}')

    # Middle Riemann Sum
    mid_x = (x_values[:-1] + x_values[1:]) / 2
    mid_heights = integrand(mid_x)
    mid_area = np.sum(dx * mid_heights)
    print(f'{part_title}: Mid Riemann Approx. Area = {mid_area}')

    # Plotting
    plt.figure(figsize=(8, 18))
    titles = ['Left', 'Right', 'Midpoint']
    for i, (x, heights, area) in enumerate(zip([left_x, right_x, mid_x], [left_heights, right_heights, mid_heights],
                                               [left_area, right_area, mid_area])):
        plt.subplot(3, 1, i + 1)
        plt.text(3, 0.7, 'Approx. Area = {:.2f}'.format(area), fontsize=12)
        plt.title(f'{part_title}: {titles[i]}-Hand Endpoint Riemann Sum with {intervals} rectangles: Approx. Area = {area:.2f}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.plot(x_values, y_values, 'pink', marker='o', markersize=marker_size, markerfacecolor='#ff5ba3')
        plt.bar(x, heights, width=(dx if i != 1 else -dx), alpha=0.1, align='edge', color='green')
        plt.grid(True)

    computation_end = time.time()
    print(f"{part_title}: Computation Time: {computation_end - computation_start:.2f} seconds")
    plt.tight_layout()
    plt.show()

# Example function f(x)
def f(x):
    return np.sin(x) + 1

compute_riemann_sum(-np.pi, np.pi, f, 4, "Part 1: a")
compute_riemann_sum(-np.pi, np.pi, f, 200, "Part 1: a")
compute_riemann_sum(-np.pi, np.pi, f, 1000, "Part 1: a")

# Different function k(x)
def k(x):
    return 3 * x + 2 * x ** 2

compute_riemann_sum(0, 1, k, 1000, "Part 1: b")

# Function g(x)
def g(x):
    return np.log(x)

compute_riemann_sum(1, np.e, g, 1000, "Part 1: c1")

# Function j(x)
def j(x):
    return x ** 2 - x ** 3

compute_riemann_sum(-1, 0, j, 1000, "Part 1: c2")

# Function R(t) for another scenario
def R(t):
    return 5.2018 * t + 4.9825

compute_riemann_sum(0, 30, R, 1000, "Part 2")
