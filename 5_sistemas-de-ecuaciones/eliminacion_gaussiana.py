import argparse
import sys

from utils import add_system_arguments, copy_matrix, format_vector, print_augmented_matrix, resolve_system_args

# Define parameters
MATRIX = "2,1,-1; -3,-1,2; -2,1,2"
VECTOR = "8,-11,-3"


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo de eliminacion gaussiana con pivoteo parcial")
    add_system_arguments(parser, MATRIX, VECTOR)
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra las matrices ampliadas por paso")
    args = parser.parse_args()
    return resolve_system_args(parser, args)


def back_substitution(matrix, vector):
    size = len(matrix)
    result = [0] * size

    for i in range(size - 1, -1, -1):
        total = vector[i]
        for j in range(i + 1, size):
            total -= matrix[i][j] * result[j]
        if matrix[i][i] == 0:
            raise ValueError("el sistema no tiene solucion unica")
        result[i] = total / matrix[i][i]

    return result


def gaussian_elimination(matrix, vector, verbose=False):
    matrix = copy_matrix(matrix)
    vector = vector[:]
    size = len(matrix)

    if verbose:
        print("Matriz ampliada inicial:")
        print_augmented_matrix(matrix, vector)

    for pivot_index in range(size - 1):
        pivot_row = max(range(pivot_index, size), key=lambda row: abs(matrix[row][pivot_index]))
        if matrix[pivot_row][pivot_index] == 0:
            raise ValueError("el sistema no tiene solucion unica")

        if pivot_row != pivot_index:
            matrix[pivot_index], matrix[pivot_row] = matrix[pivot_row], matrix[pivot_index]
            vector[pivot_index], vector[pivot_row] = vector[pivot_row], vector[pivot_index]

            if verbose:
                print()
                print(f"Intercambio F{pivot_index + 1} <-> F{pivot_row + 1}:")
                print_augmented_matrix(matrix, vector)

        for row in range(pivot_index + 1, size):
            factor = matrix[row][pivot_index] / matrix[pivot_index][pivot_index]
            for column in range(pivot_index, size):
                matrix[row][column] -= factor * matrix[pivot_index][column]
            vector[row] -= factor * vector[pivot_index]

        if verbose:
            print()
            print(f"Paso {pivot_index + 1}:")
            print_augmented_matrix(matrix, vector)

    if matrix[-1][-1] == 0:
        raise ValueError("el sistema no tiene solucion unica")

    return back_substitution(matrix, vector)


args = parse_args()
try:
    result = gaussian_elimination(args.matrix, args.vector, args.verbose)
except ValueError as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)

if args.verbose:
    print()
print(format_vector(result))
