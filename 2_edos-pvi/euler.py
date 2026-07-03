import argparse
import math
import sys

# Define parameters
A = 0
B = 3
Y0 = 1
H = 0.5
ITERATIONS = None
FUNCTION = "(t - y) / 2"


ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
ALLOWED_NAMES["abs"] = abs


def build_function(expression):
    code = compile(expression, "<function>", "eval")

    def function(t, y):
        return eval(code, {"__builtins__": {}}, {**ALLOWED_NAMES, "t": t, "y": y})

    return function


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo de Euler para PVI y' = f(t, y)")
    parser.add_argument("-a", type=float, default=A, help="Extremo izquierdo del intervalo")
    parser.add_argument("-b", type=float, default=B, help="Extremo derecho del intervalo")
    parser.add_argument("-y", "--y0", type=float, default=Y0, help="Valor inicial y(a)")
    parser.add_argument("-H", "--h", "--step", dest="h", type=float, default=H, help="Paso")
    parser.add_argument("-f", "--function", default=FUNCTION, help="Funcion f(t, y)")
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
