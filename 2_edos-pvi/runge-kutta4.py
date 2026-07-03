import argparse
import sys

from utils import add_pvi_arguments, build_function, print_step_table, resolve_pvi_steps, validate_finite

# Define parameters
A = 0
B = 3
Y0 = 1
H = 0.5
ITERATIONS = None  # Optional: if None, calculated from (B - A) / H
FUNCTION = "y * (sin(t))**3"


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo de Runge-Kutta de orden 4 para PVI y' = f(t, y)")
    add_pvi_arguments(parser, A, B, Y0, H, ITERATIONS, FUNCTION)
    args = parser.parse_args()
    resolve_pvi_steps(parser, args)

    try:
        args.function = build_function(args.function)
        args.function(args.a, args.y0)
    except Exception as exc:
        parser.error(f"--function invalida: {exc}")

    return args


def runge_kutta4(function, a, y0, h, iterations, verbose=False):
    t = a
    y = y0
    values = [(0, t, y)]

    for k in range(1, iterations + 1):
        next_t = a + k * h
        k1 = h * function(t, y)
        k2 = h * function(t + h / 2, y + k1 / 2)
        k3 = h * function(t + h / 2, y + k2 / 2)
        k4 = h * function(next_t, y + k3)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = next_t
        validate_finite(y)
        values.append((k, t, y))

    if verbose:
        print_step_table(values)

    return values


args = parse_args()
try:
    result = runge_kutta4(
        args.function,
        args.a,
        args.y0,
        args.h,
        args.iterations,
        args.verbose,
    )
except Exception as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)

if args.verbose:
    print()
print(result[-1][2])
