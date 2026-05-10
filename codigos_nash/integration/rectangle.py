import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.validate import *
from math import *

def left_area(f, I, n=1):
    valid_interval(I)
    h = (I[1] - I[0])/n
    x = lambda i: I[0] + i*h
    return sum([h*f(x(i)) for i in range(n)])
    
def right_area(f, I, n=1):
    valid_interval(I)
    h = (I[1] - I[0])/n
    x = lambda i: I[0] + i*h
    return sum([h*f(x(i)+h) for i in range(n)])

def midpoint_area(f, I, n = 1):
    valid_interval(I)
    h = (I[1]-I[0])/n
    x = lambda i: I[0] + i*h
    return sum([h*f(x(i)+h/2) for i in range(n)])

# Defines the function to integrate
def f(x):
    return sin(x)

if __name__ == "__main__":
    # Define the interval
    I = (0, pi)
    #Define the number of subintervals
    n = 100

    # Calculate the areas using different methods
    a_left = left_area(f, I, n)
    a_right = right_area(f, I, n)
    a_mid = midpoint_area(f, I, n)

    # Print the results
    print(f"Left sum:     {a_left}")
    print(f"Right sum:    {a_right}")
    print(f"Midpoint sum: {a_mid}")