import argparse
import math
import sys

import sympy as sp

# Define parameters
A = 0
B = 1
Y0 = 1
H = 0.2
ITERATIONS = None  # Optional: if None, calculated from (B - A) / H
FUNCTION = "1 + y**2"
DERIVATIVE = None  # Optional: if None, calculated as df/dt + df/dy * f


ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
ALLOWED_NAMES["abs"] = abs
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
    parser.add_argument("-a", type=float, default=A, help="Extremo izquierdo del intervalo")
    parser.add_argument("-b", type=float, default=B, help="Extremo derecho del intervalo")
    parser.add_argument("-y", "--y0", type=float, default=Y0, help="Valor inicial y(a)")
    parser.add_argument("-H", "--h", "--step", dest="h", type=float, default=H, help="Paso")
    parser.add_argument("-f", "--function", default=FUNCTION, help="Funcion f(t, y)")
    parser.add_argument("-d", "--derivative", default=DERIVATIVE, help="Funcion g(t, y) = y''. Si no se indica, se calcula con sympy")
    parser.add_argument("-i", "--iterations", type=int, default=ITERATIONS, help="Cantidad de pasos. Si no se indica, se calcula con (b-a)/h")
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra la tabla de pasos")
    args = parser.parse_args()

    if args.a >= args.b:
        parser.error("-a debe ser menor que -b")
    if args.h <= 0:
        parser.error("--h debe ser mayor a 0")
    if args.iterations is not None and args.iterations < 0:
        parser.error("--iterations debe ser mayor o igual a 0")

    if args.iterations is None:
        exact_iterations = (args.b - args.a) / args.h
        rounded_iterations = round(exact_iterations)
        if not math.isclose(exact_iterations, rounded_iterations, rel_tol=1e-12, abs_tol=1e-12):
            parser.error("(b-a)/h debe ser entero si no se indica --iterations")
        args.iterations = rounded_iterations

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
        if not math.isfinite(y):
            raise ValueError("el metodo genero un valor no finito")
        values.append((k, t, y))

    if verbose:
        print(f"{'k':<3} | {'t_k':<20} | {'y_k':<20}")
        print("-" * 49)
        for k, t, y in values:
            print(f"{k:<3} | {t:<20.12g} | {y:<20.12g}")

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
