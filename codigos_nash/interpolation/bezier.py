from math import factorial

def combinatorial(n, i):
    return factorial(n) // (factorial(i) * factorial(n - i))

def bernstein_poly(i, n, t):
    return combinatorial(n, i) * pow(t, i) * pow(1 - t, n - i)

def bezier_curve(C, t):
    n = len(C)
    result = 0
    for i in range(n):
        result += bernstein_poly(i, n - 1, t) * C[i]
    return result

if __name__ == "__main__":
    # Define the control points
    C = [0, 1, 2, 3]
    # Define the parameter t at which to evaluate the curve
    t = 0.5
    
    # Call the bezier_curve function
    value = bezier_curve(C, t)
    # Print the result
    print(f"Valor de la curva de Bézier en t = {t}: {value}")