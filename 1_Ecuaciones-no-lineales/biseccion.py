import argparse
import math

# Define parameters
A = 1
B = 2
ITERATIONS = 5
ERROR = None
FUNCTION = "x**3 - x - 2"


ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
ALLOWED_NAMES["math"] = math
ALLOWED_NAMES["abs"] = abs


def build_function(expression):
    code = compile(expression, "<function>", "eval")

    def function(x):
        return eval(code, {"__builtins__": {}}, {**ALLOWED_NAMES, "x": x})

    return function


def parse_args():
    parser = argparse.ArgumentParser(description="Metodo de biseccion")
    parser.add_argument("-a", type=float, default=A, help="Extremo izquierdo del intervalo")
    parser.add_argument("-b", type=float, default=B, help="Extremo derecho del intervalo")
    parser.add_argument("-f", "--function", default=FUNCTION, help="Funcion en terminos de x")
    parser.add_argument("-i", "--iterations", type=int, default=ITERATIONS, help="Cantidad de iteraciones")
    parser.add_argument("-e", "--error", type=float, default=ERROR, help="Error minimo para cortar. Si se indica, ignora iteraciones")
    parser.add_argument("-v", "--verbose", action="store_true", help="Muestra la tabla de iteraciones")
    args = parser.parse_args()

    if args.error is not None and args.error <= 0:
        parser.error("--error debe ser mayor a 0")
    if args.error is None and args.iterations < 0:
        parser.error("--iterations debe ser mayor o igual a 0")

    try:
        args.function = build_function(args.function)
        args.function(args.a)
        args.function(args.b)
    except Exception as exc:
        parser.error(f"--function invalida: {exc}")

    return args


def bisection(function, a, b, iterations, error, verbose=False):
    fa = function(a)
    fb = function(b)

    if fa == 0:
        return a
    if fb == 0:
        return b
    if fa * fb > 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")

    if verbose:
        print(f"{'n':<3} | {'a_n':<20} | {'b_n':<20} | {'x_n':<20} | {'f(x_n)':<20} | {'E_n':<20}")
        print("-" * 119)

    n = 0
    while error is not None or n <= iterations:
        x = (a+b) / 2
        y = function(x)
        current_error = abs(b - a) / 2

        if verbose:
            print(f"{n:<3} | {a:<20.12g} | {b:<20.12g} | {x:<20.12g} | {y:<20.12g} | {current_error:<20.12g}")

        if y == 0:
            break
        if error is not None and current_error < error:
            break
        if fa * y < 0:
            b = x
        else:
            a = x
            fa = y
        n += 1

    return x


args = parse_args()
result = bisection(args.function, args.a, args.b, args.iterations, args.error, args.verbose)

if args.verbose:
    print()
print(result)
