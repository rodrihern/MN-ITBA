import math

def taylor_second_order(f, df, interval, y0, h, N):
    t = interval[0]
    y = y0
    for i in range(N):
        y += h*f(t,y) + h**2/2*df(t,y)
        t += h
        print(f"T[{i}] = {t}, Y[{i}] = {y}")

def taylor_third_order(f , df, ddf, interval ,y0, h, N):
    t = interval[0]
    y = y0
    for i in range(N):
        y += h*f(t,y) + h**2/2*df(t,y) + h**3/6*ddf(t,y)
        t += h
        print(f"T[{i}] = {t}, Y[{i}] = {y}")

def taylor_fourth_order(f , df, ddf, dddf, interval ,y0, h, N):
    t = interval[0]
    y = y0
    for i in range(N):
        y += (h*f(t,y) + h**2/2*df(t,y) +
              h**3/6*ddf(t,y) + h**4/24*dddf(t,y))
        t += h
        print(f"T[{i}] = {t}, Y[{i}] = {y}")

# Define the function to be used in the Taylor method
def function(t, y):
    return 1+y**2

# Remember that f'(t,y) = (d/dt)f + f*((d/dy)f)
def derivative(t, y):
    return 2*(y**3) + 2*y

if __name__ == "__main__":
    # Define the parameters for the taylor method
    interval = [0, 1]
    y0 = 1
    h = 0.2
    # Remember that steps = (b - a) / h
    steps = 5
    # Call the asked taylor method
    taylor_second_order(function, derivative, interval, y0, h, steps)