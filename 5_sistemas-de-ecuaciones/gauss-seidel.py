import argparse
import sys

from utils import (
    add_system_arguments,
    format_vector,
    identity_matrix,
    infinity_norm,
    is_diagonally_dominant,
    matrix_vector_multiply,
    parse_vector,
    print_iteration_header,
    print_iteration_row,
    print_matrix,
    resolve_system_args,
    solve_lower_triangular,
    validate_initial_vector,
    validate_iteration_args,
    validate_nonzero_diagonal,
    vector_difference,
)

# Define parameters
MATRIX = "2,1; 1,-2"
VECTOR = "8,-1"
INITIAL = None  # Optional: if None, uses a zero vector
ITERATIONS = 3
ERROR = None  # Optional: if set, cut by error and ignore ITERATIONS


def gauss_seidel_method(matrix, vector, initial, iterations, error, verbose=False):
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

        for i in range(size):
            total = vector[i]
            for j in range(size):
                if i != j:
                    total -= matrix[i][j] * x[j]
            x[i] = total / matrix[i][i]

        k += 1
        current_error = infinity_norm(vector_difference(x, previous))

        if verbose:
            print_iteration_row(k, x, current_error)

        if error is not None and current_error < error:
            break

    return x


def gauss_seidel_matrix_form(matrix, vector):
    size = len(matrix)
    lower = [[matrix[i][j] if j <= i else 0 for j in range(size)] for i in range(size)]
    upper = [[matrix[i][j] if j > i else 0 for j in range(size)] for i in range(size)]
    iteration_matrix = []

    for basis_vector in identity_matrix(size):
        solved = solve_lower_triangular(lower, matrix_vector_multiply(upper, basis_vector))
        iteration_matrix.append([-value for value in solved])

    iteration_matrix = [[iteration_matrix[column][row] for column in range(size)] for row in range(size)]
    constant = solve_lower_triangular(lower, vector)
    return iteration_matrix, constant


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo de Gauss-Seidel para sistemas lineales")
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
        M, C = gauss_seidel_matrix_form(args.matrix, args.vector)
        print_matrix("M", M)
        print(f"C: {format_vector(C)}")
    else:
        result = gauss_seidel_method(args.matrix, args.vector, args.initial, args.iterations, args.error, args.verbose)
        print(format_vector(result))
except ValueError as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)
