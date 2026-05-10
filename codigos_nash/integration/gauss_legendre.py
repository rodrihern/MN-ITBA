import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.validate import *
from math import *

def non_equidistant_two_points(f, I):
    valid_interval(I)
    a = I[0]
    b = I[1]
    x = lambda t: t*(b-a)/2 + (b+a)/2
    F = lambda t: f(x(t))*(b-a)/2
    return F(-1/sqrt(3)) + F(1/sqrt(3))

def non_equidistant_three_points(f, I):
    valid_interval(I)
    a = I[0]
    b = I[1]
    x = lambda t: t*(b-a)/2 + (b+a)/2
    F = lambda t: f(x(t))*(b-a)/2
    return 5/9*F(-sqrt(3)/sqrt(5)) + 8/9*F(0) + 5/9*F(sqrt(3)/sqrt(5))

# Applies the non-equidistant two-point Gauss-Legendre quadrature to multiple subintervals
def apply_to_subintervals(f, I, n):
    h = (I[1] - I[0]) / n
    integral_approx = 0
    for i in range(n):
        I_sub = (I[0] + i*h, I[0] + (i+1)*h)
        integral_approx += non_equidistant_two_points(f, I_sub)
    return integral_approx

# Defines the function to integrate
def f(x):
    return (x**4)*cos(x)

if __name__ == "__main__":
    # Define the interval
    I = (2, 8)
    # Define the number of subintervals
    n = 3

    # Apply the method and print the result
    print("Result:", apply_to_subintervals(f, I, n))