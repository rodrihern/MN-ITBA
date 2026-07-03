import argparse
import sys

from utils import add_function_argument, print_weighted_table, validate_function, validate_interval, validate_positive_integer

# Define parameters
A = 0
B = 1
N = 1
FUNCTION = "x**2 * exp(-x**2)"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Metodo de Simpson 1/3. Usa -n 1 para la regla simple; cada panel usa 2 subintervalos."
    )
    parser.add_argument("-a", type=float, default=A, help="Extremo izquierdo del intervalo")
    parser.add_argument("-b", type=float, default=B, help="Extremo derecho del intervalo")
    add_function_argument(parser, FUNCTION)
    parser.add_argument(
        "-n",
        "--panels",
        type=int,
        default=N,
        help="Cantidad de paneles Simpson. Con n=1 se usa la regla simple",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra la tabla de evaluaciones")
    args = parser.parse_args()

    validate_interval(parser, args.a, args.b)
    validate_positive_integer(parser, args.panels, "--panels")
    args.function = validate_function(parser, args.function, args.a, args.b)

    return args


def simpson_rule(function, a, b, panels, verbose=False):
    subintervals = 2 * panels
    h = (b - a) / subintervals
    total = 0
    rows = []

    for k in range(subintervals + 1):
        x = a + k * h
        y = function(x)
        if k == 0 or k == subintervals:
            weight = 1
        elif k % 2 == 1:
            weight = 4
        else:
            weight = 2

        total += weight * y
        rows.append((k, x, y, weight))

    if verbose:
        print_weighted_table(rows)

    return h * total / 3


args = parse_args()
try:
    result = simpson_rule(args.function, args.a, args.b, args.panels, args.verbose)
except Exception as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)

if args.verbose:
    print()
print(result)
