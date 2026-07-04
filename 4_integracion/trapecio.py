import argparse
import sys

from utils import add_function_argument, print_weighted_table, validate_function, validate_interval, validate_positive_integer

# Define parameters
A = 2
B = 4
N = 1
FUNCTION = "log(x + 2)"


def trapezoid_method(function, a, b, subintervals, verbose=False):
    h = (b - a) / subintervals
    total = 0
    rows = []

    for k in range(subintervals + 1):
        x = a + k * h
        y = function(x)
        weight = 1 if k == 0 or k == subintervals else 2
        total += weight * y
        rows.append((k, x, y, weight))

    if verbose:
        print_weighted_table(rows)

    return h * total / 2


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo del trapecio. Usa -n 1 para la regla simple.")
    parser.add_argument("-a", type=float, default=A, help="Extremo izquierdo del intervalo")
    parser.add_argument("-b", type=float, default=B, help="Extremo derecho del intervalo")
    add_function_argument(parser, FUNCTION)
    parser.add_argument(
        "-n",
        "--subintervals",
        type=int,
        default=N,
        help="Cantidad de subintervalos. Con n=1 se usa la regla simple",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra la tabla de evaluaciones")
    args = parser.parse_args()

    validate_interval(parser, args.a, args.b)
    validate_positive_integer(parser, args.subintervals, "--subintervals")
    args.function = validate_function(parser, args.function, args.a, args.b)

    return args


args = parse_args()
try:
    result = trapezoid_method(args.function, args.a, args.b, args.subintervals, args.verbose)
except Exception as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)

if args.verbose:
    print()
print(result)
