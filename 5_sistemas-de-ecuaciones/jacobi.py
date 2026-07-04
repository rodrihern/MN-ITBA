import argparse
import sys

from utils import (
    add_system_arguments,
    format_vector,
    infinity_norm,
    is_diagonally_dominant,
    parse_vector,
    print_iteration_header,
    print_iteration_row,
    print_matrix,
    resolve_system_args,
    validate_initial_vector,
    validate_iteration_args,
    validate_nonzero_diagonal,
    vector_difference,
)

# Define parameters
MATRIX = "2,1; 1,-2"
VECTOR = "8,-1"
INITIAL = None
ITERATIONS = 3
ERROR = None


def jacobi_method(matrix, vector, initial, iterations, error, verbose=False):
    validate_nonzero_diagonal(matrix)
    size = len(matrix)
    x = initial[:]

    if verbose:
        if not is_diagonally_dominant(matrix):
            print("Aviso: la matriz no es diagonalmente dominante.")
            print()
        print_iteration_header(size)
        print_iteration_row(0, x, None)

    k = 0
    while error is not None or k < iterations:
        previous = x[:]
        x = [0] * size

        for i in range(size):
            total = vector[i]
            for j in range(size):
                if i != j:
                    total -= matrix[i][j] * previous[j]
            x[i] = total / matrix[i][i]

        k += 1
        current_error = infinity_norm(vector_difference(x, previous))

        if verbose:
            print_iteration_row(k, x, current_error)

        if error is not None and current_error < error:
            break

    return x


def jacobi_matrix_form(matrix, vector):
    size = len(matrix)
    iteration_matrix = [[0] * size for _ in range(size)]
    constant = [0] * size

    for i in range(size):
        if matrix[i][i] == 0:
            raise ValueError("la diagonal no puede tener ceros para este metodo")
        constant[i] = vector[i] / matrix[i][i]
        for j in range(size):
            if i != j:
                iteration_matrix[i][j] = -matrix[i][j] / matrix[i][i]

    return iteration_matrix, constant


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo de Jacobi para sistemas lineales")
    add_system_arguments(parser, MATRIX, VECTOR)
    parser.add_argument("-x", "--initial", default=INITIAL, help='Vector inicial. Si no se indica, usa ceros. Ej: "0,0"')
    parser.add_argument("-i", "--iterations", type=int, default=ITERATIONS, help="Cantidad de iteraciones")
    parser.add_argument("-e", "--error", type=float, default=ERROR, help="Error minimo para cortar. Si se indica, ignora iteraciones")
    parser.add_argument("--matrix-form", action="store_true", help="Muestra M y C para x^(k+1) = M x^(k) + C")
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra la tabla de iteraciones")
    args = parser.parse_args()
    args = resolve_system_args(parser, args)
    validate_iteration_args(parser, args)

    try:
        args.initial = [0] * len(args.vector) if args.initial is None else parse_vector(args.initial)
    except ValueError as exc:
        parser.error(f"--initial invalido: {exc}")
    validate_initial_vector(parser, args.initial, len(args.vector))

    return args


args = parse_args()
try:
    if args.matrix_form:
        M, C = jacobi_matrix_form(args.matrix, args.vector)
        print_matrix("M", M)
        print(f"C: {format_vector(C)}")
    else:
        result = jacobi_method(args.matrix, args.vector, args.initial, args.iterations, args.error, args.verbose)
        print(format_vector(result))
except ValueError as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)
