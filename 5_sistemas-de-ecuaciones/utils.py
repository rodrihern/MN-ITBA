def parse_number_list(text):
    values = []
    for part in text.replace(",", " ").split():
        values.append(float(part))
    return values


def parse_matrix(text):
    rows = []
    for raw_row in text.split(";"):
        raw_row = raw_row.strip()
        if raw_row:
            rows.append(parse_number_list(raw_row))
    return rows


def parse_vector(text):
    return parse_number_list(text)


def validate_square_system(parser, matrix, vector):
    if not matrix:
        parser.error("--matrix no puede estar vacia")

    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            parser.error("--matrix debe ser cuadrada")

    if len(vector) != n:
        parser.error("--vector debe tener la misma cantidad de elementos que filas de --matrix")


def validate_initial_vector(parser, initial, size):
    if len(initial) != size:
        parser.error("--initial debe tener la misma cantidad de elementos que filas de --matrix")


def validate_iteration_args(parser, args):
    if args.error is not None and args.error <= 0:
        parser.error("--error debe ser mayor a 0")
    if args.error is None and args.iterations < 0:
        parser.error("--iterations debe ser mayor o igual a 0")


def copy_matrix(matrix):
    return [row[:] for row in matrix]


def infinity_norm(vector):
    return max(abs(value) for value in vector)


def vector_difference(a, b):
    return [a_i - b_i for a_i, b_i in zip(a, b)]


def is_diagonally_dominant(matrix):
    for i, row in enumerate(matrix):
        diagonal = abs(row[i])
        others = sum(abs(value) for j, value in enumerate(row) if j != i)
        if diagonal < others:
            return False
    return True


def validate_nonzero_diagonal(matrix):
    for i, row in enumerate(matrix):
        if row[i] == 0:
            raise ValueError("la diagonal no puede tener ceros para este metodo")


def format_vector(vector):
    clean_values = [0 if abs(value) < 1e-14 else value for value in vector]
    return "[" + ", ".join(f"{value:.12g}" for value in clean_values) + "]"


def print_augmented_matrix(matrix, vector):
    for row, value in zip(matrix, vector):
        left = " ".join(f"{item:<14.12g}" for item in row)
        print(f"[ {left} | {value:<14.12g} ]")


def print_iteration_header(size):
    columns = ["k"] + [f"x_{i + 1}" for i in range(size)] + ["E_k"]
    print(" | ".join(f"{column:<20}" for column in columns))
    print("-" * (23 * len(columns) - 3))


def print_iteration_row(k, vector, error):
    values = [f"{k:<20}"]
    values.extend(f"{value:<20.12g}" for value in vector)
    if error is None:
        values.append(f"{'':<20}")
    else:
        values.append(f"{error:<20.12g}")
    print(" | ".join(values))


def add_system_arguments(parser, matrix_default, vector_default):
    parser.add_argument("-A", "--matrix", default=matrix_default, help='Matriz A. Filas separadas por ";". Ej: "2,1; 1,-2"')
    parser.add_argument("-b", "--vector", default=vector_default, help='Vector b. Ej: "8,-1"')


def resolve_system_args(parser, args):
    try:
        args.matrix = parse_matrix(args.matrix)
        args.vector = parse_vector(args.vector)
    except ValueError as exc:
        parser.error(f"sistema invalido: {exc}")

    validate_square_system(parser, args.matrix, args.vector)
    return args


def identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


def matrix_vector_multiply(matrix, vector):
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def solve_lower_triangular(matrix, vector):
    size = len(matrix)
    result = [0] * size
    for i in range(size):
        total = vector[i]
        for j in range(i):
            total -= matrix[i][j] * result[j]
        if matrix[i][i] == 0:
            raise ValueError("la matriz triangular inferior tiene un pivote cero")
        result[i] = total / matrix[i][i]
    return result


def print_matrix(name, matrix):
    print(f"{name}:")
    for row in matrix:
        print(format_vector(row))
