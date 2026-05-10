def newton_coeff(X, Y):
    M = []
    M.append(Y)
    n = len(Y)
    for i in range(n-1):
        last = M[i]
        next = []
        for k in range(n-i-1):
            next.append((last[k+1] - last[k]) / (X[k+i+1] - X[k]))
        M.append(next)
    return [M[i][0] for i in range(n)]

# Prints the Newton polynomial in a readable format
def print_newton_poly(X, Y):
    coef = newton_coeff(X, Y)
    for i in range(len(coef)):
        if coef[i] == 0:
            continue
        if coef[i] >= 0 and i > 0:
            print("+", end="")
        print(f"{coef[i]}", end="")
        if i > 0:
            print("*", end="")
        for j in range(i):
            if X[j] > 0:
                print(f"(x-{X[j]})", end="")
            elif X[j] < 0:
                print(f"(x+{-X[j]})", end="")
            else:
                print("x", end="")
    print("")

# Calculates the Newton polynomial at a specific point x
def newton_poly(X, Y, x):
    coeff = newton_coeff(X, Y)
    n = len(coeff)-1
    q = coeff[n]
    for i in range(n):
        q = coeff[n-i-1] + q*(x-X[n-i-1])
    return q

# Calculates the degree of the polynomial interpolator
def poly_grade(X, Y, tol=1e-12):
    coef = newton_coeff(X, Y)
    for i in range(len(coef) - 1, -1, -1):
        if abs(coef[i]) > tol:
            return i
    return 0

# Gets the values of the polynomial interpolator at n points in the interval I
def get_values(I, n, f):
    a, b = I
    h = (b - a) / (n - 1)
    X = [a + i*h for i in range(n)]
    Y = [f(xi) for xi in X]
    return X, Y

# Define the function to be used in the Newton polynomial
def f(x):
    return 1/x

# Evaluate the second derivative of the Newton polynomial at a specific point
def eval_second_dev_p(x):
    return 2*0.09861111111111126 + 0.1298765432098761*(6*x + 2.4)

if __name__ == "__main__":
    # Define the given points
    X = [0, 1, 2, 3]
    Y = [0.25, 0.55, 0.35, 2.65]

    # Get Newton coefficients and print them
    coeffs = newton_coeff(X, Y)
    print("Coeficientes de Newton:", coeffs)

    # Print the Newton polynomial
    print("Polinomio de Newton:")
    print_newton_poly(X, Y)

    # Show the grade of the polynomial interpolator (add tolerance if needed)
    print("Grado del polinomio interpolador: ", poly_grade(X, Y))