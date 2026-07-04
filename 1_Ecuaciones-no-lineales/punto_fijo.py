import argparse
import math
import sys

from utils import add_function_argument, build_function, validate_iteration_args, validate_optional_interval

# Define parameters
X0 = 1
A = None
B = None
ITERATIONS = 5
ERROR = None
FUNCTION = "(x + 1)**(1/3)"


def fixed_point_method(function, x0, a, b, iterations, error, verbose=False):
    x = x0
    validate_value(x, a, b)

    if verbose:
        print(f"{'n':<3} | {'x_n':<20} | {'E_n':<20}")
        print("-" * 49)
        print(f"{0:<3} | {x:<20.12g} | {'-':<20}")

    n = 1
    while error is not None or n <= iterations:
        previous = x
        x = function(x)
        validate_value(x, a, b)
        current_error = abs(x - previous)

        if verbose:
            print(f"{n:<3} | {x:<20.12g} | {current_error:<20.12g}")

        if error is not None and current_error < error:
            break
        n += 1

    return x


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo de punto fijo")
    parser.add_argument("-x", "--x0", type=float, default=X0, help="Valor inicial")
    parser.add_argument("-a", type=float, default=A, help="Extremo izquierdo opcional del intervalo")
    parser.add_argument("-b", type=float, default=B, help="Extremo derecho opcional del intervalo")
    add_function_argument(
        parser,
        FUNCTION,
        "Funcion g(x) despejada para la iteracion x = g(x); no es la funcion original f(x)=0",
    )
    parser.add_argument("-g", dest="function", help=argparse.SUPPRESS)
    parser.add_argument("-i", "--iterations", type=int, default=ITERATIONS, help="Cantidad de iteraciones")
    parser.add_argument("-e", "--error", type=float, default=ERROR, help="Error minimo para cortar. Si se indica, ignora iteraciones")
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra la tabla de iteraciones")
    args = parser.parse_args()

    validate_optional_interval(parser, args.a, args.b)
    if args.a is not None and not args.a <= args.x0 <= args.b:
        parser.error("--x0 debe pertenecer al intervalo [a, b]")
    validate_iteration_args(parser, args)

    try:
        args.function = build_function(args.function)
        args.function(args.x0)
        if args.a is not None:
            args.function(args.a)
            args.function(args.b)
    except Exception as exc:
        parser.error(f"--function invalida: {exc}")

    return args


def validate_value(x, a, b):
    if not math.isfinite(x):
        raise ValueError("la iteracion genero un valor no finito")
    if a is not None and not a <= x <= b:
        raise ValueError(f"el valor {x} queda fuera del intervalo [{a}, {b}]")





args = parse_args()
try:
    result = fixed_point_method(
        args.function,
        args.x0,
        args.a,
        args.b,
        args.iterations,
        args.error,
        args.verbose,
    )
except ValueError as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)

if args.verbose:
    print()
print(result)
