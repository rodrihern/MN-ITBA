import math


ALLOWED_NAMES = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")}
ALLOWED_NAMES["abs"] = abs


def build_function(expression):
    code = compile(expression, "<function>", "eval")

    def function(x):
        return eval(code, {"__builtins__": {}}, {**ALLOWED_NAMES, "x": x})

    return function


def add_function_argument(parser, default, help_text="Funcion en terminos de x"):
    parser.add_argument("-f", "--function", default=default, help=help_text)


def validate_iteration_args(parser, args):
    if args.error is not None and args.error <= 0:
        parser.error("--error debe ser mayor a 0")
    if args.error is None and args.iterations < 0:
        parser.error("--iterations debe ser mayor o igual a 0")


def validate_optional_interval(parser, a, b):
    if (a is None) != (b is None):
        parser.error("-a y -b deben indicarse juntos")
    if a is not None and a >= b:
        parser.error("-a debe ser menor que -b")
