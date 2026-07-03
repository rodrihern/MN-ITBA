import math


ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
ALLOWED_NAMES["abs"] = abs


def build_function(expression):
    code = compile(expression, "<function>", "eval")

    def function(t, y):
        return eval(code, {"__builtins__": {}}, {**ALLOWED_NAMES, "t": t, "y": y})

    return function


def add_pvi_arguments(parser, a, b, y0, h, iterations, function, verbose_help="Muestra la tabla de pasos"):
    parser.add_argument("-a", type=float, default=a, help="Extremo izquierdo del intervalo")
    parser.add_argument("-b", type=float, default=b, help="Extremo derecho del intervalo")
    parser.add_argument("-y", "--y0", type=float, default=y0, help="Valor inicial y(a)")
    parser.add_argument("-H", "--h", "--step", dest="h", type=float, default=h, help="Paso")
    parser.add_argument("-f", "--function", default=function, help="Funcion f(t, y)")
    parser.add_argument("-i", "--iterations", type=int, default=iterations, help="Cantidad de pasos. Si no se indica, se calcula con (b-a)/h")
    parser.add_argument("-v", "--verbose", action="store_true", help=verbose_help)


def resolve_pvi_steps(parser, args):
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

    return args


def validate_finite(value):
    if not math.isfinite(value):
        raise ValueError("el metodo genero un valor no finito")


def print_step_table(values):
    print(f"{'k':<3} | {'t_k':<20} | {'y_k':<20}")
    print("-" * 49)
    for k, t, y in values:
        print(f"{k:<3} | {t:<20.12g} | {y:<20.12g}")
