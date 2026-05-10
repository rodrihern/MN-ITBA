import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.validate import *
from math import *

def trapez_method(f, I, n=1):
    valid_interval(I)
    h = (I[1] - I[0])/n
    x = lambda i: I[0] + i*h
    return sum([(f(x(i)) + f(x(i+1))) * h / 2 for i in range(n)])

def trapez_error(f_prime, I, x):
    belongs(x, I)
    return f_prime(x)*pow(I[1] - I[0], 3)/12

def simpson_thirds(f, I, n=1):
    valid_interval(I)
    h = (I[1] - I[0])/(2*n)
    x = lambda i: I[0] + h*i
    return sum([(f(x(2*i)) + 4*f(x(2*i+1)) + f(x(2*i+2)))*h/3 for i in range(n)])

def simpson_third_error(f_forth, I, x):
    belongs(x, I)
    return pow((I[1]-I[0])/2, 5)*f_forth(x)/90

def simpson_three_eights(f, I):
    valid_interval(I)
    d = I[1] - I[0]
    h = d/3
    f_0 = f(I[0])
    f_1 = f(I[0]+h)
    f_2 = f(I[0]+2*h)
    f_3 = f(I[1])
    return h*(f_0 + 3*f_1 + 3*f_2 + f_3)*3/8

def simpson_three_eights_error(f_forth, I, x):
    belongs(x, I)
    return pow((I[1]-I[0])/3, 5)*f_forth(x)*3/80

# Defines the function to integrate
def f(x):
    return cosh(x)

# Simpson's 1/3 rule from a table of values
def simpson_from_table(x_vals, y_vals):
    n = len(x_vals) - 1
    if n % 2 != 0:
        raise ValueError("Number of intervals must be even for Simpson's 1/3 rule.")
    h = x_vals[1] - x_vals[0]
    result = y_vals[0] + y_vals[-1]
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * y_vals[i]
        else:
            result += 4 * y_vals[i]
    return h * result / 3

if __name__ == "__main__":
    # Define the interval
    I = (0, 2)
    # Define the n parmeter
    # Remember that the total number of subintervals is 2*n for Simpson 1/3
    n = 2
    # Define the given points 
    X = [-4, -2, 0, 2, 4, 6, 8]
    Y = [ 1,  3, 4, 4, 6, 9,14]

    # Apply the methods and print the results
    print("Result: ", simpson_thirds(f, I, n))
    print("Result: ", simpson_from_table(X, Y))

