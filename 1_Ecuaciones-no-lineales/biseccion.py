import math

# Define parameters
a = 1
b = 2
iterations = 5
error = 0
def f(x):
    return x**3 - x- 2

# start
print(f"{'n':<3} | {'a_n':<20} | {'b_n':<20} | {'x_n':<20} | {'f(x_n)':<20}")
print("-" * 96)

for n in range(0, iterations+1):
    x = (a+b) / 2
    y = f(x)
    print(f"{n:<3} | {a:<20.12g} | {b:<20.12g} | {x:<20.12g} | {y:<20.12g}")
    if y < 0:
        a = x
    else:
        b = x

print(f"\nresultado final: {x}")
