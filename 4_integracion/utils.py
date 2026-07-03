import math


ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
ALLOWED_NAMES["abs"] = abs


def build_function(expression):
    code = compile(expression, "<function>", "eval")

    def function(x):
        return eval(code, {"__builtins__": {}}, {**ALLOWED_NAMES, "x": x})

    return function


def add_function_argument(parser, default):
    parser.add_argument("-f", "--function", default=default, help="Funcion a integrar en terminos de x")


def validate_interval(parser, a, b):
    if a >= b:
        parser.error("-a debe ser menor que -b")


def validate_positive_integer(parser, value, name):
    if value <= 0:
        parser.error(f"{name} debe ser mayor a 0")


def validate_function(parser, expression, a, b):
    try:
        function = build_function(expression)
        fa = function(a)
        fb = function(b)
    except Exception as exc:
        parser.error(f"--function invalida: {exc}")

    if not math.isfinite(fa) or not math.isfinite(fb):
        parser.error("--function debe devolver valores finitos en el intervalo")

    return function


def print_weighted_table(rows):
    print(f"{'k':<3} | {'x_k':<20} | {'f(x_k)':<20} | {'peso':<10}")
    print("-" * 64)
    for k, x, y, weight in rows:
        print(f"{k:<3} | {x:<20.12g} | {y:<20.12g} | {weight:<10.12g}")
