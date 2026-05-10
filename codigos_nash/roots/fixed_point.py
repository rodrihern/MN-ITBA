import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.validate import *
import math

def fixed_point_method(g, x0, interval, iterations, tolerance):
    valid_interval(interval)
    x = x0
    iter_count = 0
    error = 0
    for i in range(iterations):
        iter_count = i
        if x < interval[0] or x > interval[1]:
            print(f"Value {x} is out of the interval {interval}")
            return
        xn = g(x)
        error = abs(xn - x)
        print(f"Iteration {i}: x = {xn}, error = {error}")
        if error < tolerance:
            print(f"Converged to {xn} after {i} iterations with error {error}")
            return
        x = xn
    print(f"Root found at x = {x} after {iter_count} iterations with error = {error}")
    return

# Define the g(x) = x function for f(x) = 0
# g's fixed point is the root of f
# Check that |g'(x)| < 1 in the interval
def g_func(x):
    return x * math.cosh(10 / x) - 6

def g_func2(x):
    return math.sqrt((10-(x**3))/4)

if __name__ == "__main__":
    # Define the parameters for the fixed point method
    x0 = 1
    interval = [1, 2]
    iterations = 100
    tolerance = 10**-5
    # Call the fixed point method
    fixed_point_method(g_func2, x0, interval, iterations, tolerance)