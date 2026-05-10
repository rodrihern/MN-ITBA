import math

def heun_method(f, interval, y0, h, M):
    T = [0] * (M+1)
    Y = [0] * (M+1)
    T[0] = interval[0]
    Y[0] = y0
    for i in range(M):
        T[i+1] = T[i] + h
        k1 = h * f(T[i], Y[i])
        k2 = h * f(T[i+1], Y[i] + k1)
        Y[i+1] = Y[i] + (k1 + k2) / 2
    return T, Y

# Define the function to be used in the Heun method
def function(t, y):
    return t - y

if __name__ == "__main__":
    # Define the parameters for the heun method
    interval = [0, 1]
    y0 = 3
    h = 0.1
    # Remember that steps = (b - a) / h
    steps = 10
    # Call the asked taylor method
    T, Y = heun_method(function, interval, y0, h, steps)
    # Print the results
    for i in range(len(T)):
        print(f"T[{i}] = {T[i]}, Y[{i}] = {Y[i]}")