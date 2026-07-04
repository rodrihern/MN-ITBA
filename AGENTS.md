# Instrucciones para Metodos Numericos

Estas instrucciones aplican en `/Users/rodri/ITBA/metodos` cuando el usuario pida resolver ejercicios, migrar codigo desde `codigos_nash`, o editar scripts nuevos de metodos numericos.

## Prioridades

1. Para resolver ejercicios, usar primero los scripts nuevos del tema correspondiente.
2. Si todavia no existe script nuevo para el metodo, usar `codigos_nash`.
3. Cuando se cree o edite codigo nuevo, seguir las convenciones de este archivo.
4. Todo codigo nuevo o migrado debe verificarse contra el legacy equivalente en `codigos_nash` antes de terminar.

No crear scripts nuevos para resolver un ejercicio si ya hay una forma razonable de hacerlo con los scripts existentes. Crear o modificar codigo solo si el usuario lo pide, si se esta migrando un metodo, o si no hay forma razonable de resolver el caso con lo existente.

## Scripts nuevos

Los scripts nuevos se corren desde `/Users/rodri/ITBA/metodos`.

| Metodo | Archivo | Argumentos principales |
|---|---|---|
| Biseccion | `1_Ecuaciones-no-lineales/biseccion.py` | `-f`, `-a`, `-b`, `-i`, `-e`, `-v` |
| Newton | `1_Ecuaciones-no-lineales/newton-raphson.py` | `-f`, `-d`, `-s`, `-x`, `-a`, `-b`, `-i`, `-e`, `-v` |
| Punto fijo | `1_Ecuaciones-no-lineales/punto_fijo.py` | `-f`, `-x`, `-a`, `-b`, `-i`, `-e`, `-v` |
| Euler | `2_edos-pvi/euler.py` | `-f`, `-a`, `-b`, `-y`, `-H`, `-i`, `-v` |
| Heun orden 2 | `2_edos-pvi/heun2.py` | `-f`, `-a`, `-b`, `-y`, `-H`, `-i`, `-v` |
| Taylor orden 2 | `2_edos-pvi/taylor2.py` | `-f`, `-d`, `-a`, `-b`, `-y`, `-H`, `-i`, `-v` |
| Runge-Kutta orden 4 | `2_edos-pvi/runge-kutta4.py` | `-f`, `-a`, `-b`, `-y`, `-H`, `-i`, `-v` |
| Interpolacion Lagrange | `3_interpolacion/lagrange.py` | `-x`, `-y`, `-p`, `-e`, `-v` |
| Interpolacion Newton | `3_interpolacion/newton.py` | `-x`, `-y`, `-p`, `-e`, `-v` |
| Rectangulo | `4_integracion/rectangulo.py` | `-f`, `-a`, `-b`, `-n`, `-m`, `-v` |
| Trapecio | `4_integracion/trapecio.py` | `-f`, `-a`, `-b`, `-n`, `-v` |
| Simpson 1/3 | `4_integracion/simpson.py` | `-f`, `-a`, `-b`, `-n`, `-v` |
| Gauss-Legendre | `4_integracion/gauss_legendre.py` | `-f`, `-a`, `-b`, `-p`, `-n`, `-v` |
| Eliminacion gaussiana | `5_sistemas-de-ecuaciones/eliminacion_gaussiana.py` | `-A`, `-b`, `-v` |
| Jacobi | `5_sistemas-de-ecuaciones/jacobi.py` | `-A`, `-b`, `-x`, `-i`, `-e`, `--matrix-form`, `-v` |
| Gauss-Seidel | `5_sistemas-de-ecuaciones/gauss-seidel.py` | `-A`, `-b`, `-x`, `-i`, `-e`, `--matrix-form`, `-v` |

## Convenciones para codigo nuevo

Todo script nuevo o migrado desde `codigos_nash` debe seguir este formato:

- Usar `argparse` para argumentos CLI.
- Definir parametros editables arriba del archivo en mayusculas, por ejemplo `A`, `B`, `X0`, `Y0`, `H`, `ITERATIONS`, `ERROR`, `FUNCTION`.
- Usar esos parametros como defaults de `argparse`, para que el script funcione tanto editando el archivo como pasando argumentos.
- Separar el codigo en funciones: `parse_args()`, una funcion del metodo numerico, y helpers como `build_function(...)` o `build_functions(...)` si hacen falta.
- Reutilizar helpers comunes de la carpeta en `utils.py` cuando reduzcan duplicacion clara, por ejemplo parsing de puntos, funciones matematicas seguras, validaciones compartidas, argumentos CLI repetidos o tablas verbose.
- Si varios scripts de una misma carpeta comparten interfaz, extraer el armado de esos argumentos a helpers tipo `add_*_arguments(...)` o `resolve_*_args(...)`. Cada script debe seguir mostrando en `--help` solamente los argumentos que realmente usa.
- No mover la formula principal del metodo a `utils.py` ni forzar un parser generico si los argumentos del metodo son distintos. Es preferible tener helpers chicos y componibles antes que un parser comun que acepte flags que despues se ignoran.
- En scripts de ecuaciones no lineales, usar `-f` / `--function` como argumento principal para la funcion de iteracion o evaluacion. En punto fijo, `-f` debe documentar claramente que recibe `g(x)` para `x = g(x)`, no la funcion original `f(x) = 0`.
- En scripts de interpolacion, mantener la interfaz comun `-p` / `--points` para puntos, `-e` / `--eval` para evaluar el polinomio, y `-v` / `--verbose` para mostrar la tabla o terminos auxiliares. Aceptar puntos como `0,1` y como `"(0,1)"`; si hay valores negativos con parentesis, recordar que se deben pasar entre comillas por el shell.
- Al final del archivo, parsear argumentos, ejecutar el metodo e imprimir el resultado.
- Agregar `-v` / `--verbose` para mostrar tabla de iteraciones o pasos.
- Sin `-v`, imprimir solamente el resultado final que se debe usar.
- En metodos de PVI, la tabla de `--verbose` debe seguir la tabla del apartado `### Calculadora` del metodo correspondiente en `notas/` (por ejemplo, para Euler, Taylor 2 y Heun: `k`, `t_k`, `y_k`).
- Si el metodo acepta corte por iteraciones y por error/tolerancia, las condiciones deben ser exclusivas:
  - Si el usuario pasa `-e` / `--error`, ignorar iteraciones y cortar solo por error.
  - Si el usuario no pasa error, cortar solo por iteraciones.
- Validar argumentos con `parser.error(...)` cuando sea posible: error mayor a 0, iteraciones no negativas, intervalos validos, paso positivo, datos obligatorios del metodo.
- Para errores durante la ejecucion, imprimir mensajes cortos sin traceback y salir con codigo distinto de 0.
- Para funciones matematicas pasadas por CLI, aceptar expresiones en terminos de la variable del metodo sin requerir `math.`, por ejemplo `sin(x)`, `exp(x)`, `sqrt(x)`.
- Exponer nombres seguros de `math` y deshabilitar `__builtins__` cuando se evalue una expresion.
- No agregar `math` como nombre permitido si el usuario quiere evitar el formato `math.sin(x)`.
- Si el metodo necesita derivadas, usar `sympy` para calcularlas automaticamente desde la funcion cuando sea razonable. Mantener argumentos opcionales para sobrescribir derivadas manualmente, como `-d` y `-s`.
- Usar tablas de ancho fijo con f-strings en verbose, alineadas a la izquierda:

```python
print(f"{'n':<3} | {'x_n':<20} | {'E_n':<20}")
print(f"{n:<3} | {x:<20.12g} | {error:<20.12g}")
```

## Helpers por carpeta

Usar helpers de `utils.py` solo dentro de la carpeta del tema correspondiente.

- `1_Ecuaciones-no-lineales/utils.py`: funciones matematicas seguras en variable `x`, argumento comun `-f` / `--function`, validacion de `-i` / `-e`, validacion de intervalo opcional.
- `2_edos-pvi/utils.py`: funciones matematicas seguras en variables `t` e `y`, argumentos comunes de PVI (`-a`, `-b`, `-y`, `-H`, `-f`, `-i`, `-v`), resolucion de pasos, validacion de valores finitos y tabla verbose `k | t_k | y_k`.
- `3_interpolacion/utils.py`: parsing comun de puntos y listas para `-p`, `-x`, `-y`, `-e`, `-v`.
- `4_integracion/utils.py`: funciones matematicas seguras en variable `x`, argumento comun `-f` / `--function`, validacion de intervalo, validacion de `-n` y tablas verbose.
- `5_sistemas-de-ecuaciones/utils.py`: parsing comun de matrices y vectores para `-A`, `-b`, `-x`, validacion de sistemas cuadrados, norma infinito, formato de vectores y tablas verbose.

No importar helpers entre carpetas distintas si eso mezcla convenciones de variables o argumentos. Por ejemplo, `build_function` de ecuaciones no lineales usa `x`, mientras que el de PVI usa `t, y`.

## Verificacion obligatoria de codigo nuevo

Despues de crear o editar un script nuevo que reemplaza un metodo de `codigos_nash`, verificarlo contra el archivo legacy correspondiente antes de terminar.

Checklist minimo:

- Correr al menos un caso comparable con el script nuevo.
- Correr el mismo caso con la funcion legacy de `codigos_nash`, normalmente importandola desde `python3 -c`.
- Si el archivo legacy tiene un ejemplo hardcodeado en `if __name__ == "__main__"`, correr tambien ese ejemplo y reproducirlo con el script nuevo.
- Comparar el valor final numerico.
- Comparar el error reportado cuando aplique.
- Probar `-v` / `--verbose` y confirmar que la tabla se imprime bien.
- Probar sin `-v` y confirmar que imprime solo el resultado final.
- Probar modo por iteraciones.
- Probar modo por error/tolerancia, confirmando que ignora iteraciones.
- Probar al menos un error de entrada importante del metodo y confirmar que el script muestra un mensaje corto sin traceback.
- Si hay una diferencia con `codigos_nash`, no copiar automaticamente el comportamiento legacy. Revisar si el legacy usa una convencion incorrecta, documentar la diferencia y dejar el codigo nuevo con la convencion matematicamente consistente.

## Como correr scripts nuevos

Biseccion por iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/biseccion.py -f "x**3 - x - 2" -a 1 -b 2 -i 5 -v
```

Biseccion por error, ignorando iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/biseccion.py -f "x**3 - x - 2" -a 1 -b 2 -e 0.001 -v
```

Newton por iteraciones con derivadas automaticas:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/newton-raphson.py -f "x**3 - x - 2" -x 1.5 -i 5 -v
```

Newton por error, ignorando iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/newton-raphson.py -f "x**3 - x - 2" -x 1.5 -e 0.001 -v
```

Newton con derivada manual opcional:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/newton-raphson.py -f "x**3 - x - 2" -d "3*x**2 - 1" -s "6*x" -x 1.5 -i 5 -v
```

Punto fijo por iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/punto_fijo.py -f "(x + 1)**(1/3)" -x 1 -i 5 -v
```

Punto fijo por error, ignorando iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/punto_fijo.py -f "sqrt((10 - x**3)/4)" -x 1 -a 1 -b 2 -e 0.00001 -v
```

Euler:

```bash
cd /Users/rodri/ITBA/metodos
python3 2_edos-pvi/euler.py -f "(t - y) / 2" -a 0 -b 3 -y 1 -H 0.5 -v
```

Heun orden 2:

```bash
cd /Users/rodri/ITBA/metodos
python3 2_edos-pvi/heun2.py -f "t - y" -a 0 -b 1 -y 3 -H 0.1 -v
```

Taylor orden 2 con derivada automatica:

```bash
cd /Users/rodri/ITBA/metodos
python3 2_edos-pvi/taylor2.py -f "1 + y**2" -a 0 -b 1 -y 1 -H 0.2 -v
```

Runge-Kutta orden 4:

```bash
cd /Users/rodri/ITBA/metodos
python3 2_edos-pvi/runge-kutta4.py -f "y * (sin(t))**3" -a 0 -b 3 -y 1 -H 0.5 -v
```

Interpolacion de Newton con puntos:

```bash
cd /Users/rodri/ITBA/metodos
python3 3_interpolacion/newton.py -p 0,0.25 1,0.55 2,0.35 3,2.65 -v
```

Interpolacion de Lagrange evaluando el polinomio:

```bash
cd /Users/rodri/ITBA/metodos
python3 3_interpolacion/lagrange.py -p 0,0.25 1,0.55 2,0.35 3,2.65 -e 1.5
```

Rectangulo simple con punto medio (`-n 1`):

```bash
cd /Users/rodri/ITBA/metodos
python3 4_integracion/rectangulo.py -f "exp(x)" -a 0 -b 1 -n 1 -m midpoint -v
```

Rectangulo compuesto:

```bash
cd /Users/rodri/ITBA/metodos
python3 4_integracion/rectangulo.py -f "exp(x)" -a 0 -b 1 -n 4 -m midpoint -v
```

Trapecio simple (`-n 1`):

```bash
cd /Users/rodri/ITBA/metodos
python3 4_integracion/trapecio.py -f "log(x+2)" -a 2 -b 4 -n 1 -v
```

Trapecio compuesto:

```bash
cd /Users/rodri/ITBA/metodos
python3 4_integracion/trapecio.py -f "log(x+2)" -a 2 -b 4 -n 4 -v
```

Simpson 1/3 simple (`-n 1`, un panel de Simpson):

```bash
cd /Users/rodri/ITBA/metodos
python3 4_integracion/simpson.py -f "x**2 * exp(-x**2)" -a 0 -b 1 -n 1 -v
```

Simpson 1/3 compuesto (`-n` indica cantidad de paneles de Simpson, cada panel usa 2 subintervalos):

```bash
cd /Users/rodri/ITBA/metodos
python3 4_integracion/simpson.py -f "x**2 * exp(-x**2)" -a 0 -b 1 -n 2 -v
```

Gauss-Legendre simple de 2 puntos (`-n 1`):

```bash
cd /Users/rodri/ITBA/metodos
python3 4_integracion/gauss_legendre.py -f "exp(x)" -a 0 -b 1 -p 2 -n 1 -v
```

Gauss-Legendre simple de 3 puntos (`-n 1`):

```bash
cd /Users/rodri/ITBA/metodos
python3 4_integracion/gauss_legendre.py -f "exp(x)" -a 0 -b 1 -p 3 -n 1 -v
```

Gauss-Legendre compuesto (`-n` indica cantidad de subintervalos):

```bash
cd /Users/rodri/ITBA/metodos
python3 4_integracion/gauss_legendre.py -f "x**4 * cos(x)" -a 2 -b 8 -p 2 -n 3 -v
```

Eliminacion gaussiana:

```bash
cd /Users/rodri/ITBA/metodos
python3 5_sistemas-de-ecuaciones/eliminacion_gaussiana.py -A "2,1,-1; -3,-1,2; -2,1,2" -b "8,-11,-3" -v
```

Jacobi por iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 5_sistemas-de-ecuaciones/jacobi.py -A "2,1; 1,-2" -b "8,-1" -x "0,0" -i 3 -v
```

Jacobi por error, ignorando iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 5_sistemas-de-ecuaciones/jacobi.py -A "26,2,2; 3,27,3; 2,3,17" -b "12.6,-14.3,6" -x "0,0,0" -e 0.001 -v
```

Jacobi en forma matricial:

```bash
cd /Users/rodri/ITBA/metodos
python3 5_sistemas-de-ecuaciones/jacobi.py -A "2,1; 1,-2" -b "8,-1" --matrix-form
```

Gauss-Seidel por iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 5_sistemas-de-ecuaciones/gauss-seidel.py -A "2,1; 1,-2" -b "8,-1" -x "0,0" -i 3 -v
```

Gauss-Seidel por error, ignorando iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 5_sistemas-de-ecuaciones/gauss-seidel.py -A "26,2,2; 3,27,3; 2,3,17" -b "12.6,-14.3,6" -x "0,0,0" -e 0.001 -v
```

Gauss-Seidel en forma matricial:

```bash
cd /Users/rodri/ITBA/metodos
python3 5_sistemas-de-ecuaciones/gauss-seidel.py -A "2,1; 1,-2" -b "8,-1" --matrix-form
```

## Archivos legacy de codigos_nash

Usar estos archivos solo cuando todavia no exista script nuevo para el metodo, o para verificar/corroborar codigo nuevo.

| Metodo | Archivo | Funcion principal |
|---|---|---|
| Biseccion | `codigos_nash/roots/bisection.py` | `bisection_method(f, interval, iterations, err)` |
| Newton | `codigos_nash/roots/newton_raphson.py` | `newton_raphson(f, df, x0, iterations, tolerance)` |
| Punto fijo | `codigos_nash/roots/fixed_point.py` | `fixed_point_method(g, x0, interval, iterations, tolerance)` |
| Euler | `codigos_nash/ivp/euler.py` | `euler_method(f, interval, y_0, h, M)` |
| Heun | `codigos_nash/ivp/heun.py` | `heun_method(f, interval, y0, h, M)` |
| Taylor orden 2 | `codigos_nash/ivp/taylor.py` | `taylor_second_order(f, df, interval, y0, h, N)` |
| Taylor orden 3 | `codigos_nash/ivp/taylor.py` | `taylor_third_order(f, df, ddf, interval, y0, h, N)` |
| Taylor orden 4 | `codigos_nash/ivp/taylor.py` | `taylor_fourth_order(f, df, ddf, dddf, interval, y0, h, N)` |
| RK4 | `codigos_nash/ivp/runge_kutta.py` | `rk4(f, interval, y0, h, M)` |
| Euler orden 2 | `codigos_nash/ivp/euler_second.py` | `euler_second_method(f, interval, y_0, y_p_0, h, M)` |
| Trapecio / Simpson / Newton-Cotes | `codigos_nash/integration/newton_cotes.py` | `trapez_method`, `simpson_thirds`, `simpson_three_eights`, `simpson_from_table` |
| Rectangulos | `codigos_nash/integration/rectangle.py` | `left_area`, `right_area`, `midpoint_area` |
| Gauss-Legendre | `codigos_nash/integration/gauss_legendre.py` | `non_equidistant_two_points`, `non_equidistant_three_points`, `apply_to_subintervals` |
| Interpolacion Lagrange | `codigos_nash/interpolation/lagrange.py` | `lagrange_poly`, `lagrange_error` |
| Interpolacion Newton | `codigos_nash/interpolation/newton.py` | `newton_coeff`, `newton_poly`, `poly_grade`, `get_values` |
| Bezier | `codigos_nash/interpolation/bezier.py` | `bezier_curve` |
| Eliminacion gaussiana | `codigos_nash/linear_algebra/gaussian_elimination.py` | `gaussian_elimination` |
| Jacobi / Gauss-Seidel | `codigos_nash/linear_algebra/lu_decomposition.py` | `jacobi`, `gauss_seidel` |

## Como correr codigos_nash

Los archivos legacy suelen tener ejemplos hardcodeados en `if __name__ == "__main__"`. Para casos especificos, conviene importar la funcion desde `python3 -c` y pasar lambdas.

Biseccion:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/roots'); from bisection import bisection_method; bisection_method(lambda x: x**3-x-2, [1,2], 100, 1e-5)"
```

Newton:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/roots'); from newton_raphson import newton_raphson; newton_raphson(lambda x: x**3-x-2, lambda x: 3*x**2-1, 1.5, 100, 1e-5)"
```

Punto fijo:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/roots'); from fixed_point import fixed_point_method; fixed_point_method(lambda x: (x+2)**(1/3), 1.5, [1,2], 100, 1e-5)"
```

Euler / Heun / RK4:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/ivp'); from euler import euler_method; T,Y=euler_method(lambda t,y: t-y, [0,1], 3, 0.1, 10); print(T); print(Y)"
```

Para Heun cambiar `from euler import euler_method` por `from heun import heun_method`. Para RK4 usar `from runge_kutta import rk4`.

Taylor:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/ivp'); from taylor import taylor_second_order; taylor_second_order(lambda t,y: 1+y**2, lambda t,y: 2*y*(1+y**2), [0,1], 1, 0.2, 5)"
```

Integracion:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/integration'); from newton_cotes import trapez_method; print(trapez_method(lambda x: math.exp(x*x), (0,3), 10))"
```

Rectangulos:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/integration'); from rectangle import midpoint_area; print(midpoint_area(lambda x: math.sin(x), (0, math.pi), 100))"
```

Gauss-Legendre:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/integration'); from gauss_legendre import non_equidistant_two_points; print(non_equidistant_two_points(lambda x: x**4*math.cos(x), (2,8)))"
```

## Flujo para resolver ejercicios

1. Identificar el metodo pedido y los datos del enunciado.
2. Revisar el script correspondiente antes de responder.
3. Correr el codigo localmente cuando sea posible.
4. Si existe script nuevo para el metodo, resolver con ese script y explicar como correrlo.
5. Si no existe script nuevo, resolver con `codigos_nash`.
6. Si hay dudas por convencion, usar `codigos_nash` para corroborar y explicar cualquier diferencia.

## Formato para respuestas de ejercicios

Responder en espanol, directo y practico. Incluir siempre:

- Resultado final con coma decimal si tiene decimales.
- Comando exacto desde `/Users/rodri/ITBA/metodos`.
- Valores exactos pasados al script.
- Linea de salida que contiene el valor que debe usarse.
- Valor final para entregar en un bloque fenced `text` solo con el valor.
- Limitacion concreta si el codigo no reproduce exactamente el enunciado.

Formato recomendado:

````text
Resultado:
<resultado final con coma decimal si tiene decimales>

Codigo:
<comando exacto desde /Users/rodri/ITBA/metodos>
Salida: <linea relevante>

Para entregar:
```text
<solo el valor final a entregar con coma decimal si tiene decimales>
```

Notas:
<aclaraciones importantes, si hacen falta>
````

Usar siempre coma decimal en los resultados finales que se muestran al usuario (`0,125`, no `0.125`). Las salidas crudas de Python pueden mostrarse con punto si asi las imprime el programa, pero en `Resultado` y `Para entregar` convertir a coma decimal.

Cuando el resultado final requiera una cantidad fija de decimales, mostrar tanto el valor truncado como el redondeado. Si el enunciado pide explicitamente truncar, redondear, parte entera o coma decimal, mostrar ese como "para entregar".

Al final de cada respuesta incluir un bloque fenced `text` que contenga solamente el valor final a entregar, sin etiqueta, explicacion ni unidades extra.

## Convenciones matematicas importantes

- En punto fijo se debe ingresar `g(x)` para la iteracion `x = g(x)`, no la funcion original `f(x) = 0`.
- En PVI, si el enunciado da paso `h`, calcular `N = (b-a)/h` cuando el codigo use cantidad de pasos.
- Para ecuaciones diferenciales de segundo orden, convertir a sistema:

```text
u1 = y
u2 = y'
u1' = u2
u2' = expresion despejada de y''
```

## Cuando el enunciado o el legacy tenga problemas

Si el enunciado parece inconsistente, decirlo claramente antes de dar una respuesta alternativa.

Ejemplos:

- Si una ecuacion no tiene raiz real.
- Si un despeje de punto fijo diverge.
- Si el metodo solicitado no converge con los datos dados.
- Si el codigo existente no puede representar el caso sin editar un archivo hardcodeado.
- Si un codigo usa una convencion distinta a la del enunciado.
- Si `codigos_nash` tiene un bug o reporta un valor inconsistente con el error calculado.

En esos casos, explicar que se corrio, que paso, y cual es la interpretacion o correccion mas probable solo si corresponde.

## Estilo

No llenar la respuesta con teoria innecesaria. Incluir solo la transformacion matematica necesaria para justificar que se esta ingresando la funcion correcta.

Siempre distinguir entre:

- El valor que devuelve el codigo.
- El valor final truncado.
- El valor final redondeado.
- Cual de esos valores corresponde entregar segun el enunciado.
- El valor final con coma decimal cuando tenga decimales.
