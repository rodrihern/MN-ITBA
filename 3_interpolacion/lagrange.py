import argparse
import sys

from utils import add_interpolation_arguments, resolve_interpolation_points

# Define parameters
X_VALUES = [0.0, 0.4, 0.8, 1.2]
Y_VALUES = [1.0, 0.921061, 0.696707, 0.362358]
POINTS = None
EVAL_POINT = None


def parse_args():
    parser = argparse.ArgumentParser(description="Interpolacion de Lagrange")
    add_interpolation_arguments(parser, POINTS, EVAL_POINT, "Muestra los terminos de Lagrange")
    args = parser.parse_args()
    return resolve_interpolation_points(parser, args, X_VALUES, Y_VALUES)


def lagrange_basis_value(i, x_values, point):
    result = 1
    for j, x_j in enumerate(x_values):
        if j != i:
            result *= (point - x_j) / (x_values[i] - x_j)
    return result


def lagrange_value(x_values, y_values, point):
    result = 0
    for i, y_i in enumerate(y_values):
        result += y_i * lagrange_basis_value(i, x_values, point)
    return result


def format_factor(value):
    if value == 0:
        return "x"
    if value > 0:
        return f"(x - {value:.12g})"
    return f"(x + {-value:.12g})"


def basis_denominator(i, x_values):
    denominator = 1
    for j, x_j in enumerate(x_values):
        if j != i:
            denominator *= x_values[i] - x_j
    return denominator


def format_lagrange_basis(i, x_values):
    numerator_factors = [format_factor(x_j) for j, x_j in enumerate(x_values) if j != i]
    numerator = "*".join(numerator_factors)
    denominator = basis_denominator(i, x_values)
    return f"({numerator}) / ({denominator:.12g})"


def format_lagrange_polynomial(x_values, y_values):
    terms = []
    for i, y_i in enumerate(y_values):
        terms.append(f"{y_i:.12g}*{format_lagrange_basis(i, x_values)}")
    return " + ".join(terms).replace("+ -", "- ")


def print_points(x_values, y_values):
    print(f"{'i':<3} | {'x_i':<20} | {'y_i':<20}")
    print("-" * 49)
    for i, (x_i, y_i) in enumerate(zip(x_values, y_values)):
        print(f"{i:<3} | {x_i:<20.12g} | {y_i:<20.12g}")


def print_basis_terms(x_values, y_values):
    print(f"{'i':<3} | {'y_i':<20} | {'L_i(x)':<60}")
    print("-" * 91)
    for i, y_i in enumerate(y_values):
        print(f"{i:<3} | {y_i:<20.12g} | {format_lagrange_basis(i, x_values):<60}")


def lagrange_interpolation(x_values, y_values, point=None, verbose=False):
    polynomial = format_lagrange_polynomial(x_values, y_values)

    if verbose:
        print_points(x_values, y_values)
        print()
        print_basis_terms(x_values, y_values)
        print()
        print(f"Polinomio: {polynomial}")

    if point is None:
        return polynomial
    return lagrange_value(x_values, y_values, point)


args = parse_args()
try:
    result = lagrange_interpolation(
        args.x_values,
        args.y_values,
        args.eval,
        args.verbose,
    )
except Exception as exc:
    print(f"Error: {exc}", file=sys.stderr)
    sys.exit(1)

if args.verbose:
    print()
print(result)
