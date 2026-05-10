def delta_poly(i, X, x):
    p = 1
    for x_k in X:
        if x_k != X[i]:
            p *= (x - x_k) / (X[i] - x_k)
    return p

def lagrange_poly(X, Y, x):
    L = 0
    for i in range(len(Y)):
        L += Y[i] * delta_poly(i, X, x)
    return L

def lagrange_error(K, X, x):
    e = K
    for i in range(len(X)):
        e *= (x-X[i])/(i+1)
    return abs(e) 

if __name__ == "__main__":
    # Define the given points
    X = [-1, -0.7, -0.1, 0.5, 1]
    Y = [-1.9, -1.051, 0.701, 2.525, 4.1]
    # Define the evaluation point
    x_eval = 0.2
    # Calculate the Lagrange polynomial at the evaluation point
    p_val = lagrange_poly(X, Y, x_eval)
    # Print the result
    print(f"p({x_eval}) = {p_val}")