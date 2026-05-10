def square_matrix(A):
    n = len(A)
    for i in range(n):
        if len(A[i]) != n:
            print("Matrix is not square")
            return

def upper_triangular(M):
    for i in range(len(M)):
        for j in range(i):
            if M[i][j] != 0:
                print("Matrix is not in upper triangular form")
                return

# A must be in upper triangular square matrix
def backwards_substitution(A, b): 
    square_matrix(A)
    upper_triangular(A)
    n = len(A)
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j]*x[j]
        if A[i][i] == 0:
            print("Matrix is singular")
            return
        x[i] /= A[i][i]
    return x

# A must be a square matrix
def gaussian_elimination(A, b): 
    square_matrix(A)
    n = len(A)
    for i in range(n-1):
        for k in range(i+1, n):
            coef = A[k][i]/A[i][i]
            A[k] = [A[k][j] - A[i][j]*coef for j in range(n)]
            b[k] -= b[i]*coef
    return backwards_substitution(A, b)

if __name__ == "__main__":
    # Define the system of equations as a matrix A
    A = [
        [25, 5, 1],
        [64, 8, 1],
        [144, 12, 1]
    ]
    # Define the results of the equations as a vector b
    b = [106.8, 177.2, 279.2]

    # Print the matrix and vector
    print("A matrix:")
    for row in A:
        print(row)
    print("b vector:", b)

    # Solve the system using Gaussian elimination
    x = gaussian_elimination([row[:] for row in A], b[:])
    
    # Print the solution
    if x is not None:
        print("Ax = b solution:")
        for i, val in enumerate(x):
            print(f"x[{i}] = {val}")
    else:
        print("System couldn't be solved.")