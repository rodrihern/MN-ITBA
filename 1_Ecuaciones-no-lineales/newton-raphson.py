import argparse
import math
import sys
import sympy as sp

# Define parameters
A = 1
B = 2
X0 = None
ITERATIONS = 5
ERROR = None
FUNCTION = "x**3 - x - 2"
DERIVATIVE = None
SECOND_DERIVATIVE = None


ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
ALLOWED_NAMES["abs"] = abs
SYMPY_NAMES = {name: getattr(sp, name) for name in dir(sp) if not name.startswith("_")}
SYMPY_NAMES["abs"] = sp.Abs


def build_functions(function_expression, derivative_expression=None, second_derivative_expression=None):
    x = sp.symbols("x")
    locals_by_name = {**SYMPY_NAMES, "x": x}

    function_symbolic = sp.sympify(function_expression, locals=locals_by_name)
    derivative_symbolic = sp.sympify(derivative_expression, locals=locals_by_name) if derivative_expression else sp.diff(function_symbolic, x)
    second_derivative_symbolic = sp.sympify(second_derivative_expression, locals=locals_by_name) if second_derivative_expression else sp.diff(derivative_symbolic, x)

    function = sp.lambdify(x, function_symbolic, modules=[ALLOWED_NAMES, "math"])
    derivative = sp.lambdify(x, derivative_symbolic, modules=[ALLOWED_NAMES, "math"])
    second_derivative = sp.lambdify(x, second_derivative_symbolic, modules=[ALLOWED_NAMES, "math"])

    return function, derivative, second_derivative


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo de Newton-Raphson")
    parser.add_argument("-a", type=float, default=A, help="Extremo izquierdo usado si no se indica x0")
    parser.add_argument("-b", type=float, default=B, help="Extremo derecho usado si no se indica x0")
    parser.add_argument("-x", "--x0", type=float, default=X0, help="Valor inicial")
    parser.add_argument("-f", "--function", default=FUNCTION, help="Funcion en terminos de x")
    parser.add_argument("-d", "--derivative", default=DERIVATIVE, help="Derivada en terminos de x. Si no se indica, se calcula con sympy")
    parser.add_argument("-s", "--second-derivative", default=SECOND_DERIVATIVE, help="Segunda derivada en terminos de x. Si no se indica, se calcula con sympy")
    parser.add_argument("-i", "--iterations", type=int, default=ITERATIONS, help="Cantidad de iteraciones")
    parser.add_argument("-e", "--error", type=float, default=ERROR, help="Error minimo para cortar. Si se indica, ignora iteraciones")
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra la tabla de iteraciones")
    args = parser.parse_args()

    if args.error is not None and args.error <= 0:
        parser.error("--error debe ser mayor a 0")
    if args.error is None and args.iterations < 0:
        parser.error("--iterations debe ser mayor o igual a 0")

    try:
        args.function, args.derivative, args.second_derivative = build_functions(
            args.function,
            args.derivative,
            args.second_derivative,
        )

        values_to_test = [args.a, args.b]
        if args.x0 is not None:
            values_to_test.append(args.x0)

        for value in values_to_test:
            args.function(value)
            args.derivative(value)
            args.second_derivative(value)
    except Exception as exc:
        parser.error(f"expresion invalida: {exc}")

    return args


def choose_initial_value(function, second_derivative, a, b):
    if function(a) * second_derivative(a) > 0:
        return a
    return b


def newton_raphson(function, derivative, x0, iterations, error, verbose=False):
    x = x0

    if verbose:
        print(f"{'n':<3} | {'x_n':<20} | {'E_n':<20}")
        print("-" * 49)
        print(f"{0:<3} | {x:<20.12g} | {'-':<20}")

    n = 1
    while error is not None or n <= iterations:
        derivative_value = derivative(x)
        if derivative_value == 0:
            raise ZeroDivisionError("La derivada vale 0, no se puede continuar")

        previous = x
        x = x - function(x) / derivative_value
        current_error = abs(previous - x)

        if verbose:
            print(f"{n:<3} | {x:<20.12g} | {current_error:<20.12g}")

        if error is not None and current_error < error:
            break
        n += 1

    return x


args = parse_args()
x0 = args.x0
if x0 is None:
    x0 = choose_initial_value(args.function, args.second_derivative, args.a, args.b)

try:
    result = newton_raphson(args.function, args.derivative, x0, args.iterations, args.error, args.verbose)
except ZeroDivisionError as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)

if args.verbose:
    print()
print(result)
