import argparse
import sys

from utils import add_pvi_arguments, build_function, print_step_table, resolve_pvi_steps, validate_finite

# Define parameters
A = 0
B = 3
Y0 = 1
H = 0.5
ITERATIONS = None  # Optional: if None, calculated from (B - A) / H
FUNCTION = "(t - y) / 2"


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo de Euler para PVI y' = f(t, y)")
    add_pvi_arguments(parser, A, B, Y0, H, ITERATIONS, FUNCTION)
    args = parser.parse_args()
    resolve_pvi_steps(parser, args)

    try:
        args.function = build_function(args.function)
        args.function(args.a, args.y0)
    except Exception as exc:
        parser.error(f"--function invalida: {exc}")

    return args


def euler(function, a, y0, h, iterations, verbose=False):
    t = a
    y = y0
    values = [(0, t, y)]

    for k in range(1, iterations + 1):
        y = y + h * function(t, y)
        t = a + k * h
        validate_finite(y)
        values.append((k, t, y))

    if verbose:
        print_step_table(values)

    return values


args = parse_args()
try:
    result = euler(
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
