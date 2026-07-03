import argparse
import sys
from typing import Optional

from utils import add_interpolation_arguments, resolve_interpolation_points

# Define parameters
X_VALUES = [0.0, 0.4, 0.8, 1.2]
Y_VALUES = [1.0, 0.921061, 0.696707, 0.362358]
POINTS = None
EVAL_POINT = None


Table = list[list[Optional[float]]]


def parse_args():
    parser = argparse.ArgumentParser(description="Interpolacion de Newton con tabla de diferencias divididas")
    add_interpolation_arguments(parser, POINTS, EVAL_POINT, "Muestra la tabla de diferencias divididas")
    args = parser.parse_args()
    return resolve_interpolation_points(parser, args, X_VALUES, Y_VALUES)


def divided_differences_table(x_values, y_values):
    n = len(x_values)
    table: Table = [[None for _ in range(n + 1)] for _ in range(n)]

    for i in range(n):
        table[i][0] = x_values[i]
        table[i][1] = y_values[i]

    for j in range(2, n + 1):
        for i in range(n - j + 1):
            numerator = table_value(table, i + 1, j - 1) - table_value(table, i, j - 1)
            denominator = table_value(table, i + j - 1, 0) - table_value(table, i, 0)
            table[i][j] = numerator / denominator

    return table


def table_value(table: Table, row, column):
    value = table[row][column]
    if value is None:
        raise ValueError("la tabla de diferencias divididas tiene una celda vacia inesperada")
    return value


def newton_coefficients(table):
    return [table_value(table, 0, j) for j in range(1, len(table) + 1)]


def evaluate_newton_polynomial(coefficients, x_values, point):
    result = coefficients[-1]
    for i in range(len(coefficients) - 2, -1, -1):
        result = coefficients[i] + result * (point - x_values[i])
    return result


def format_factor(value):
    if value == 0:
        return "x"
    if value > 0:
        return f"(x - {value:.12g})"
    return f"(x + {-value:.12g})"


def format_newton_polynomial(coefficients, x_values):
    terms = []
    for i, coefficient in enumerate(coefficients):
        if coefficient == 0:
            continue
        factors = "".join(format_factor(x_values[j]) for j in range(i))
        if factors:
            terms.append(f"{coefficient:.12g}{factors}")
        else:
            terms.append(f"{coefficient:.12g}")
    return " + ".join(terms).replace("+ -", "- ")


def print_table(table):
    headers = ["x", "y"] + [f"DD{j}" for j in range(1, len(table))]
    print(" | ".join(f"{header:<20}" for header in headers))
    print("-" * (23 * len(headers) - 3))

    for row in table:
        formatted = []
        for value in row:
            if value is None:
                formatted.append(f"{'':<20}")
            else:
                formatted.append(f"{value:<20.12g}")
        print(" | ".join(formatted))


def newton_interpolation(x_values, y_values, point=None, verbose=False):
    table = divided_differences_table(x_values, y_values)
    coefficients = newton_coefficients(table)
    polynomial = format_newton_polynomial(coefficients, x_values)

    if verbose:
        print_table(table)
        print()
        print(f"Coeficientes: {coefficients}")
        print(f"Polinomio: {polynomial}")

    if point is None:
        return polynomial
    return evaluate_newton_polynomial(coefficients, x_values, point)


args = parse_args()
try:
    result = newton_interpolation(
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
