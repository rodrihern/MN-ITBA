import argparse
import sys

import sympy as sp

from utils import ALLOWED_NAMES, add_pvi_arguments, print_step_table, resolve_pvi_steps, validate_finite

# Define parameters
A = 0
B = 1
Y0 = 1
H = 0.2
ITERATIONS = None  # Optional: if None, calculated from (B - A) / H
FUNCTION = "1 + y**2"
DERIVATIVE = None  # Optional: if None, calculated as df/dt + df/dy * f


SYMPY_NAMES = {name: getattr(sp, name) for name in dir(sp) if not name.startswith("_")}
SYMPY_NAMES["abs"] = sp.Abs


def build_functions(function_expression, derivative_expression=None):
    t, y = sp.symbols("t y")
    locals_by_name = {**SYMPY_NAMES, "t": t, "y": y}

    function_symbolic = sp.sympify(function_expression, locals=locals_by_name)
    if derivative_expression:
        derivative_symbolic = sp.sympify(derivative_expression, locals=locals_by_name)
    else:
        derivative_symbolic = sp.diff(function_symbolic, t) + sp.diff(function_symbolic, y) * function_symbolic

    function = sp.lambdify((t, y), function_symbolic, modules=[ALLOWED_NAMES, "math"])
    derivative = sp.lambdify((t, y), derivative_symbolic, modules=[ALLOWED_NAMES, "math"])

    return function, derivative


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo de Taylor de orden 2 para PVI y' = f(t, y)")
    add_pvi_arguments(parser, A, B, Y0, H, ITERATIONS, FUNCTION)
    parser.add_argument("-d", "--derivative", default=DERIVATIVE, help="Funcion g(t, y) = y''. Si no se indica, se calcula con sympy")
    args = parser.parse_args()
    resolve_pvi_steps(parser, args)

    try:
        args.function, args.derivative = build_functions(args.function, args.derivative)
        args.function(args.a, args.y0)
        args.derivative(args.a, args.y0)
    except Exception as exc:
        parser.error(f"expresion invalida: {exc}")

    return args


def taylor2(function, derivative, a, y0, h, iterations, verbose=False):
    t = a
    y = y0
    values = [(0, t, y)]

    for k in range(1, iterations + 1):
        y = y + h * function(t, y) + h**2 / 2 * derivative(t, y)
        t = a + k * h
        validate_finite(y)
        values.append((k, t, y))

    if verbose:
        print_step_table(values)

    return values


args = parse_args()
try:
    result = taylor2(
        args.function,
        args.derivative,
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
