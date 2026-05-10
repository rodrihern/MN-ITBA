import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.validate import *
from ivp import euler_method

def back_and_forth_err(f, interval, y_0, h, m):
    T, Y = euler_method(f, interval, y_0, h, m)
    neg_interval = [interval[1], interval[0]]
    T, Z = euler_method(f, neg_interval, Y[m], h, m)
    print(f"Euler method back and forth error: {abs(Z[m] - y_0)}")

def half_step_err(f, interval, y_0, h, m):
    T, Y1 = euler_method(f, interval, y_0, h, m)
    T, Y2 = euler_method(f, interval, y_0, h, 2*m)
    print(f"Euler method back and forth error: {[abs(Y1[i] - Y2[2*i]) for i in range(m + 1)]}")

# Define the function to be used in the Euler method
def fun(t, y):
    return -0.2*(y**2) + 10

if __name__ == "__main__":
    # Define the parameters for the euler method
    interval = [0, 0.5]
    y0 = 1
    # Remember that steps = (b - a) / h
    h = 0.1
    steps = 5
    # Call the euler method
    back_and_forth_err(fun, interval, y0, h, steps)
    half_step_err(fun, interval, y0, h, steps)
    