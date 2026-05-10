import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.validate import *
import math

def bisection_method(f, interval, iterations, err):
    if not valid_interval(interval) or not bolzano_condition(f, interval):
        print("Invalid interval or Bolzano condition not satisfied.")
        return
    a = interval[0]
    b = interval[1]
    error = interval[1] - interval[0]
    iter_count = 0
    for i in range(iterations+1):
        c = (a + b) / 2
        if f(c) == 0:
            break
        error = abs(b - a) / 2
        if error < err:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count = i + 1
        print(f"Iteration {iter_count}: x = {c}, error = {error}")
    print(f"Root found at x = {c} after {iter_count} iterations with error = {error}")

# Define function to find the root of here
def function(x):
    return ((9.8*80)/x)*(1-math.exp(-(x/80)*4))-5


if __name__ == "__main__":
    # Define the parameters for the bisection method
    interval = [156, 157]
    # Use a high number of iterations if it is not known
    iterations = 4
    error = 10**-6
    # Call the bisection method
    bisection_method(function, interval, iterations, error)
