import argparse
import math
import sys

from utils import add_function_argument, validate_function, validate_interval, validate_positive_integer

# Define parameters
A = 0
B = 1
POINTS = 2
N = 1
FUNCTION = "exp(x)"


def gauss_legendre_method(function, a, b, points, subintervals, verbose=False):
    h = (b - a) / subintervals
    base_nodes_weights = gauss_nodes_weights(points)
    result = 0
    rows = []

    for k in range(subintervals):
        left = a + k * h
        right = left + h
        midpoint = (left + right) / 2
        half_width = (right - left) / 2

        for local_node, local_weight in base_nodes_weights:
            x = midpoint + local_node * half_width
            weight = local_weight * half_width
            y = function(x)
            contribution = weight * y
            result += contribution
            rows.append((k, x, y, weight, contribution))

    if verbose:
        print(f"{'k':<3} | {'x':<20} | {'f(x)':<20} | {'peso':<20} | {'aporte':<20}")
        print("-" * 96)
        for k, x, y, weight, contribution in rows:
            print(f"{k:<3} | {x:<20.12g} | {y:<20.12g} | {weight:<20.12g} | {contribution:<20.12g}")

    return result



def parse_args():
    parser = argparse.ArgumentParser(description="Cuadratura de Gauss-Legendre. Usa -n 1 para la regla simple.")
    parser.add_argument("-a", type=float, default=A, help="Extremo izquierdo del intervalo")
    parser.add_argument("-b", type=float, default=B, help="Extremo derecho del intervalo")
    add_function_argument(parser, FUNCTION)
    parser.add_argument("-p", "--points", type=int, choices=[2, 3], default=POINTS, help="Cantidad de puntos de Gauss")
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


def gauss_nodes_weights(points):
    if points == 2:
        node = 1 / math.sqrt(3)
        return [(-node, 1), (node, 1)]

    node = math.sqrt(3 / 5)
    return [(-node, 5 / 9), (0, 8 / 9), (node, 5 / 9)]





args = parse_args()
try:
    result = gauss_legendre_method(args.function, args.a, args.b, args.points, args.subintervals, args.verbose)
except Exception as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)

if args.verbose:
    print()
print(result)
