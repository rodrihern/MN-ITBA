import math

def euler_method(f, interval, y_0, h, M):
    Y = [0] * (M+1)
    T = [0] * (M+1)
    Y[0] = y_0
    T[0] = interval[0]
    for i in range(M):
        T[i+1] = T[i] + h
        k1 = h * f(T[i], Y[i])
        Y[i+1] = Y[i] + k1
    return T, Y

# Define the function to be used in the Euler method
def function(t, y):
    return (t**3)*y - 1.25*y

if __name__ == "__main__":
    # Define the parameters for the euler method
    interval = [0, 2]
    y0 = 1
    # Remember that steps = (b - a) / h
    h = 0.25
    steps = 8
    # Call the euler method
    T, Y = euler_method(function, interval, y0, h, steps)
    # Print the results
    for i in range(len(T)):
        print(f"T[{i}] = {T[i]}, Y[{i}] = {Y[i]}")