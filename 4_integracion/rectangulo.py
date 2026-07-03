import argparse
import sys

from utils import add_function_argument, validate_function, validate_interval, validate_positive_integer

# Define parameters
A = 0
B = 1
N = 1
MODE = "midpoint"
FUNCTION = "exp(x)"


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo del rectangulo. Usa -n 1 para la regla simple.")
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
    parser.add_argument(
        "-m",
        "--mode",
        choices=["left", "right", "midpoint"],
        default=MODE,
        help="Punto usado como altura del rectangulo",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra la tabla de evaluaciones")
    args = parser.parse_args()

    validate_interval(parser, args.a, args.b)
    validate_positive_integer(parser, args.subintervals, "--subintervals")
    args.function = validate_function(parser, args.function, args.a, args.b)

    return args


def rectangle_rule(function, a, b, subintervals, mode, verbose=False):
    h = (b - a) / subintervals
    result = 0
    rows = []

    for k in range(subintervals):
        left = a + k * h
        right = left + h

        if mode == "left":
            x = left
        elif mode == "right":
            x = right
        else:
            x = (left + right) / 2

        y = function(x)
        result += h * y
        rows.append((k, x, y))

    if verbose:
        print(f"{'k':<3} | {'x':<20} | {'f(x)':<20}")
        print("-" * 49)
        for k, x, y in rows:
            print(f"{k:<3} | {x:<20.12g} | {y:<20.12g}")

    return result


args = parse_args()
try:
    result = rectangle_rule(args.function, args.a, args.b, args.subintervals, args.mode, args.verbose)
except Exception as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)

if args.verbose:
    print()
print(result)
