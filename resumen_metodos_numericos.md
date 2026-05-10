# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Implementations of numerical methods for the ITBA course *Métodos Numéricos*. Two independent codebases cover the same methods:

- `codigos_nash/` — Python
- `codigos_marengo/` — Octave/MATLAB

Both are used to cross-verify exercise answers. See `AGENTS.md` for the full workflow on how to answer exercises.

## Running codigos_nash (Python)

Nash files have hardcoded examples in `if __name__ == "__main__"` blocks. **Do not run files directly.** Import the function and pass lambdas:

```bash
python3 -c "
import sys; sys.path.insert(0, 'codigos_nash/roots')
from bisection import bisection_method
bisection_method(lambda x: x**3 - x - 2, [1, 2], 100, 1e-5)
"
```

For IVP methods that return `(T, Y)` lists, access the result at index `N`:

```bash
python3 -c "
import sys; sys.path.insert(0, 'codigos_nash/ivp')
from euler import euler_method
T, Y = euler_method(lambda t, y: t - y, [0, 1], 3, 0.1, 10)
print(Y[10])
"
```

## Running codigos_marengo (Octave)

Always run from `/Users/rodri/ITBA/metodos` with `addpath`:

```bash
octave --quiet --eval "format long; addpath('codigos_marengo'); [k,X,E] = biseccion(@(x) x^3-x-2, 1, 2, 1e-5, 1000); X(end)"
```

For IVP methods, `Y(end)` or `Y(N+1)` is the final value. For root methods, `X(end)` is the last iterate (or `X(k+1)` for the k-th step).

## Function signatures

### codigos_nash

| Method | Function | Signature |
|--------|----------|-----------|
| Bisection | `bisection_method(f, interval, iterations, err)` | `interval=[a,b]` |
| Newton | `newton_raphson(f, df, x0, iterations, tolerance)` | — |
| Fixed point | `fixed_point_method(g, x0, interval, iterations, tolerance)` | `interval=[a,b]` |
| Euler | `euler_method(f, interval, y_0, h, M)` → `(T, Y)` | `M` = steps |
| Heun | `heun_method(f, interval, y0, h, M)` → `(T, Y)` | — |
| Taylor ord 2 | `taylor_second_order(f, df, interval, y0, h, N)` | prints, no return |
| Taylor ord 3 | `taylor_third_order(f, df, ddf, interval, y0, h, N)` | prints, no return |
| Taylor ord 4 | `taylor_fourth_order(f, df, ddf, dddf, interval, y0, h, N)` | prints, no return |
| RK4 | `rk4(f, interval, y0, h, M)` → `(T, Y)` | — |

### codigos_marengo

| Method | Signature | Returns |
|--------|-----------|---------|
| `biseccion(f,a,b,prec,maxiter)` | stop by error: large maxiter; stop by steps: small prec | `[k, X, E]` |
| `newton(f,fp,x0,prec,maxiter)` | — | `[k, X, E]` |
| `puntofijo(g,x0,prec,maxiter)` | pass `g` not `f`; `X(1)=x0` so `X(n+1)` is `xn` | `[k, X, E]` |
| `euler(f,a,b,ya,N)` | `N` = steps, `h=(b-a)/N` | `[T, Y]` |
| `heun(f,a,b,ya,N)` | same as euler | `[T, Y]` |
| `taylor2(f,fp,a,b,ya,N)` | `fp` = total derivative of f | `[T, Y]` |
| `taylor3(f,fp,fpp,a,b,ya,N)` | — | `[T, Y]` |
| `taylor4(f,fp,fpp,fppp,a,b,ya,N)` | — | `[T, Y]` |
| `rk4(f,a,b,ya,N)` | — | `[T, Y]` |
| `jacobi(A,Y,X0,prec,maxiter)` | — | `[k, X, E]` |
| `gseid(A,Y,X0,prec,maxiter)` | — | `[k, X, E]` |
| `simpsoncomp(f,a,b,subint)` | `subint` must be even | `S` (scalar) |

## Key conventions

**Step count vs step size:** Nash IVP functions take `h` (step size) and `M` (number of steps). Marengo IVP functions take `N` (number of steps) and compute `h=(b-a)/N` internally. If given `h`, compute `N = (b-a)/h`.

**Fixed point:** Both codebases expect `g(x)` (the despeje `x = g(x)`), not `f(x)`. In Marengo, `X(1) = x0`, so the n-th iterate is `X(n+1)`.

**Taylor derivatives:** The `fp`, `fpp`, etc. arguments are **total derivatives** of `f(t,y)` along trajectories, not partial derivatives. For `f(t,y)`, `fp = ∂f/∂t + f·∂f/∂y`.

**Systems (2nd order ODEs):** Convert to first-order system `u1=y, u2=y'` before using any IVP method. `ya` in Marengo and `y_0` in Nash accept vectors for systems.
