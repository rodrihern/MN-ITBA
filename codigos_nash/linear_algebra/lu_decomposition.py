from gaussian_elimination import square_matrix

def jacobi(A, b, x_0, iterations): 
    square_matrix(A)
    n = len(A)
    x = [x_i for x_i in x_0]
    for k in range(iterations):
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if j != i:
                    x[i] -= x_0[j]*A[i][j]
            if A[i][i] == 0:
                print("Matrix is not diagonally dominant")
                return
            x[i] /= A[i][i]
        x_0 = [x_i for x_i in x]
    return x

def gauss_seidel(A, b, x_0, iterations): 
    square_matrix(A)
    n = len(A)
    x = x_0
    for k in range(iterations):
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if j != i:
                    x[i] -= x[j]*A[i][j]
            if A[i][i] == 0:
                print("Matrix is not diagonally dominant")
                return
            x[i] /= A[i][i]
    return x

if __name__ == "__main__":
    # Define the system of equations as a matrix A
    A = [
        [26, 2, 2],
        [3, 27, 3],
        [2, 3, 17]
    ]
    # Define the results of the equations as a vector b
    b = [12.6, -14.3, 6]
    # Define the initial values
    x0 = [0, 0, 0]
    # Define the number of iterations
    iterations = 5

    # Print the matrix and vector
    print("A matrix:")
    for row in A:
        print(row)
    print("b vector:", b)

    # Print the result for Jacobi's Method
    print("\nJacobi's Method:")
    x_jacobi = jacobi(A, b, x0, iterations)
    if x_jacobi is not None:
        for i, val in enumerate(x_jacobi):
            print(f"x[{i}] = {val}")

    # Print the result for Gauss-Seidel's Method
    print("\nGauss-Seidel's Method:")
    x_gauss_seidel = gauss_seidel(A, b, x0, iterations)
    if x_gauss_seidel is not None:
        for i, val in enumerate(x_gauss_seidel):
            print(f"x[{i}] = {val}")