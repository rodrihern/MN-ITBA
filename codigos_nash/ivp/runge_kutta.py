from math import *

def rk4(f, interval, y0, h, M):
    T = [0] * (M+1)
    Y = [0] * (M+1)
    T[0] = interval[0]
    Y[0] = y0
    for j in range(M):
        T[j+1] = T[j] + h
        k1 = h * f(T[j], Y[j])
        k2 = h * f(T[j] + h/2, Y[j] + k1/2)
        k3 = h * f(T[j] + h/2, Y[j] + k2/2)
        k4 = h * f(T[j+1], Y[j] + k3)
        Y[j+1] = Y[j] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return T, Y

# Define the function to be used in the Runge-Kutta method
def function(t, y):
    return y * ((sin(t))**3)

if __name__ == "__main__":
    # Define the parameters for the runge_kutta method
    interval = [0, 3]
    y0 = 1
    h = 0.5
    # Remember that steps = (b - a) / h
    steps = 6
    # Call the asked taylor method
    T, Y = rk4(function, interval, y0, h, steps)
    # Print the results
    for i in range(len(T)):
        print(f"T[{i}] = {T[i]}, Y[{i}] = {Y[i]}")