import math

def euler_second_method(f, interval, y_0, y_p_0, h, M):
    Y = [0] * (M+1)
    T = [0] * (M+1)
    G = [0] * (M+1)
    Y[0] = y_0
    T[0] = interval[0]
    G[0] = y_p_0
    for i in range(M):
        T[i+1] = T[i] + h
        k1 = h * G[i]
        k2 = h * f(T[i], Y[i], G[i])
        Y[i+1] = Y[i] + k1
        G[i+1] = G[i] + k2
    return T, Y

# Define the function to be used in the Euler method
def function(t, y, dy):
    return 10*math.sin(t) - 5*dy - 6*y

if __name__ == "__main__":
    # Define the parameters for the euler method
    interval = [0, 3]
    y0 = 0
    yp0 = 5
    steps = 30
    # Remember that steps = (b - a) / h
    h = 0.1
    # Call the euler method
    T, Y = euler_second_method(function, interval, y0, yp0, h, steps)
    # Print the results
    for i in range(len(T)):
        print(f"T[{i}] = {T[i]}, Y[{i}] = {Y[i]}")