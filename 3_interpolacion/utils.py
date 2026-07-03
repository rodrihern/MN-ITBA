def parse_float_list(values):
    numbers = []
    for value in values:
        parts = value.split(",")
        for part in parts:
            part = part.strip()
            if part:
                numbers.append(float(part))
    return numbers


def parse_points(values):
    points = []
    for value in values:
        cleaned = value.strip().strip("()[]")
        parts = [part.strip() for part in cleaned.split(",")]
        if len(parts) != 2 or not parts[0] or not parts[1]:
            raise ValueError(f"punto invalido: {value}")
        points.append((float(parts[0]), float(parts[1])))
    return points


def add_interpolation_arguments(parser, points_default, eval_default, verbose_help):
    parser.add_argument("-x", "--x-values", nargs="+", default=None, help="Valores de x separados por espacios o comas")
    parser.add_argument("-y", "--y-values", nargs="+", default=None, help="Valores de y separados por espacios o comas")
    parser.add_argument(
        "-p",
        "--points",
        nargs="+",
        default=points_default,
        help='Puntos como pares x,y o "(x,y)". Ejemplo: -p 0,1 "(0.4,0.921061)"',
    )
    parser.add_argument("-e", "--eval", type=float, default=eval_default, help="Punto donde evaluar el polinomio")
    parser.add_argument("-v", "--verbose", action="store_true", help=verbose_help)


def resolve_interpolation_points(parser, args, default_x_values, default_y_values):
    if args.points is not None and (args.x_values is not None or args.y_values is not None):
        parser.error("--points no se puede combinar con --x-values ni --y-values")
    if (args.x_values is None) != (args.y_values is None):
        parser.error("--x-values y --y-values deben indicarse juntos")

    try:
        if args.points is not None:
            points = parse_points(args.points)
            args.x_values = [point[0] for point in points]
            args.y_values = [point[1] for point in points]
        else:
            args.x_values = parse_float_list(args.x_values) if args.x_values is not None else default_x_values
            args.y_values = parse_float_list(args.y_values) if args.y_values is not None else default_y_values
    except ValueError as exc:
        parser.error(f"valores invalidos: {exc}")

    if len(args.x_values) != len(args.y_values):
        parser.error("--x-values y --y-values deben tener la misma cantidad de valores")
    if len(args.x_values) < 2:
        parser.error("se necesitan al menos 2 puntos")
    if len(set(args.x_values)) != len(args.x_values):
        parser.error("los valores de x no pueden repetirse")

    return args
