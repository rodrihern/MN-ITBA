---
name: metodos-numericos
description: Use when the user asks to solve numerical methods exercises in /Users/rodri/ITBA/metodos — bisection, Newton, fixed point, IVP (Euler, Heun, Taylor, RK4). Requires running codigos_nash and codigos_marengo to verify the answer before responding.
---

# Numerical Methods — Exercise Solving

## Objective

Every response must include:

1. The final result of the exercise.
2. How to reproduce it with `codigos_nash` and `codigos_marengo` (both, for corroboration).

Do not create new scripts if an existing code file can be used. Only modify or create code if the user explicitly asks for it.

## Files to use

**codigos_nash** (Python):

| Method | File |
|--------|---------|
| Bisection | `codigos_nash/roots/bisection.py` |
| Newton | `codigos_nash/roots/newton_raphson.py` |
| Fixed point | `codigos_nash/roots/fixed_point.py` |
| Euler | `codigos_nash/ivp/euler.py` |
| Heun | `codigos_nash/ivp/heun.py` |
| Taylor | `codigos_nash/ivp/taylor.py` |
| RK4 | `codigos_nash/ivp/runge_kutta.py` |

**codigos_marengo** (Octave):

| Method | File |
|--------|---------|
| Bisection | `codigos_marengo/biseccion.m` |
| Newton | `codigos_marengo/newton.m` |
| Fixed point | `codigos_marengo/puntofijo.m` |
| Euler | `codigos_marengo/euler.m` |
| Heun | `codigos_marengo/heun.m` |
| Taylor order 2 | `codigos_marengo/taylor2.m` |
| Taylor order 3 | `codigos_marengo/taylor3.m` |
| Taylor order 4 | `codigos_marengo/taylor4.m` |
| RK4 | `codigos_marengo/rk4.m` |

## How to run each one

**codigos_nash:** import the function and pass lambdas from `python3 -c`, because the files have hardcoded examples in `if __name__ == "__main__"`.

```bash
python3 -c "
import sys; sys.path.insert(0, 'codigos_nash/roots')
from bisection import bisection
print(bisection(lambda x: x**3 - x - 2, 1, 2, 1e-5))
"
```

**codigos_marengo:** run with Octave from `/Users/rodri/ITBA/metodos`:

```bash
octave --quiet --eval "format long; addpath('codigos_marengo'); biseccion(@(x) x^3-x-2, 1, 2, 1e-5)"
```

Before responding, read the corresponding method file to understand the exact parameters each function accepts.

## Important conventions

- **Fixed point (nash/marengo):** the program asks for `f(x)`, but enter `g(x)` in the form `x = g(x)`.
- **Marengo fixed point:** `x0` corresponds to the upper endpoint `b`. If the statement gives `x0 = 0.5`, enter `b = 0.5`.
- **Marengo vectors:** several methods return complete vectors. In fixed point, `X(1) = x0`, so `X(7)` is `x6`.
- **IVP with step h:** compute `N = (b - a) / h`.

## Higher-order IVPs

For second-order differential equations, convert to a system:

```
u1 = y,  u2 = y'
u1' = u2
u2' = [expression solved for y'']
```

## Response format

Respond in Spanish, directly. Structure:

```
Resultado:
<resultado final>

codigos_nash:
<exact command from /Users/rodri/ITBA/metodos>
Salida: <relevant output line>

codigos_marengo:
<exact command from /Users/rodri/ITBA/metodos>
Salida: <relevant output line>

Para entregar (copiar y pegar):
<valor con coma decimal, ej: 1,2345>

Notas:
<only if something important needs to be noted>
```

**"Para entregar" block:** always use comma (,) as the decimal separator. Show the truncated and rounded values. If the statement explicitly asks for one of the two, indicate it.

Example final block:

```
Para entregar (copiar y pegar):
  Truncado:   1,2345
  Redondeado: 1,2346
```

## When there are problems

If the exercise statement seems inconsistent (no real root, divergence, method does not converge), say so before giving an alternative answer. Explain what was run, what happened, and the most likely interpretation.

If a code file cannot reproduce the case without editing a hardcoded file, say so and explain the limitation.

## Style

Do not include unnecessary theory. Include only the mathematical transformation needed to justify that the correct function is being entered. Always distinguish between: code output, truncated value, rounded value, and which value should be submitted.
