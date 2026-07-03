# Instrucciones para responder ejercicios de Metodos Numericos

Estas instrucciones aplican cuando el usuario pida resolver ejercicios de metodos numericos en este workspace.

## Objetivo de la respuesta

Cada respuesta debe incluir dos cosas:

1. La solucion del ejercicio, con el resultado final en el formato pedido por el enunciado.
2. Como reproducir ese resultado usando los scripts nuevos del tema correspondiente. Si todavia no existe script nuevo para ese metodo, usar los codigos existentes de `codigos_nash`.

No crear scripts nuevos para resolver un ejercicio si un codigo existente puede usarse. Solo modificar o crear codigo si el usuario lo pide explicitamente, o si no existe ninguna forma razonable de hacerlo con los archivos existentes. Cuando el usuario pida migrar o reemplazar codigos de `codigos_nash`, el codigo nuevo debe seguir el formato estandar definido abajo.

## Flujo recomendado

1. Identificar el metodo pedido y los datos del enunciado.
2. Revisar el archivo correspondiente antes de responder, porque los scripts tienen parametros por defecto arriba y argumentos CLI especificos.
3. Correr el codigo localmente cuando sea posible.
4. Si existe script nuevo para el metodo, usar ese script para resolver y explicar como correrlo.
5. Si no existe script nuevo todavia, usar `codigos_nash` para resolver y corroborar el resultado.

## Formato recomendado de respuesta

Responder en espanol, directo y practico:

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

Es importante que este en un unico bloque de texto para que se pueda copiar solamente la respuesta

Notas:
<aclaraciones importantes, si hacen falta>
````

Usar siempre coma decimal en los resultados finales que se muestran al usuario (`0,125`, no `0.125`). Las salidas crudas de Python pueden mostrarse con punto si asi las imprime el programa, pero en `Resultado` y `Para entregar` convertir a coma decimal. Cuando el resultado final tenga una cantidad fija de decimales, mostrar tanto el valor truncado como el redondeado. Si el enunciado pide explicitamente truncar, redondear, parte entera o coma decimal, indicar cual corresponde entregar.
Al final de cada respuesta incluir un bloque fenced `text` que contenga solamente el valor final a entregar, sin etiqueta, explicacion ni unidades extra, para que el usuario pueda copiarlo y pegarlo directamente.

En la respuesta incluir:

- El comando exacto desde `/Users/rodri/ITBA/metodos`.
- Los valores exactos que hay que pasar.
- Que linea de salida contiene el valor que debe usarse.
- La limitacion concreta si algun codigo no reproduce exactamente el enunciado.

## Scripts nuevos

Estos scripts son la referencia principal cuando existan. Se corren desde `/Users/rodri/ITBA/metodos`.

| Metodo | Archivo | Argumentos principales |
|---|---|---|
| Biseccion | `1_Ecuaciones-no-lineales/biseccion.py` | `-f`, `-a`, `-b`, `-i`, `-e`, `-v` |
| Newton | `1_Ecuaciones-no-lineales/newton-raphson.py` | `-f`, `-d`, `-s`, `-x`, `-a`, `-b`, `-i`, `-e`, `-v` |

## Formato estandar para codigo nuevo

Cuando se cree o migre un script para reemplazar algo de `codigos_nash`, usar este formato:

- Imports al principio. Usar `argparse` para argumentos CLI.
- Parametros editables arriba del archivo en mayusculas, por ejemplo `A`, `B`, `ITERATIONS`, `ERROR`, `FUNCTION`.
- Los valores de arriba deben ser los defaults de `argparse`, asi el script sirve tanto editando el archivo como pasando argumentos.
- Agregar `-v` / `--verbose` para mostrar tabla. Sin `-v`, imprimir solamente el resultado final.
- Si el metodo acepta condicion de corte por iteraciones y por error, deben ser exclusivas:
  - Si el usuario pasa `-e` / `--error`, ignorar iteraciones y cortar solo por error.
  - Si el usuario no pasa error, cortar solo por iteraciones.
- Validar argumentos con `parser.error(...)`: error mayor a 0, iteraciones no negativas, y cualquier dato obligatorio del metodo.
- Para funciones matematicas pasadas por CLI, aceptar expresiones en terminos de `x` sin requerir `math.`, por ejemplo `sin(x)`, `exp(x)`, `sqrt(x)`.
- Exponer nombres seguros de `math` en el evaluador y deshabilitar `__builtins__`.
- No agregar `math` como nombre permitido si el usuario quiere evitar el formato `math.sin(x)`.
- Si el metodo necesita derivadas, usar `sympy` para calcularlas automaticamente desde `-f` cuando sea razonable. Mantener argumentos opcionales como `-d` y `-s` para que el usuario pueda sobrescribir la derivada o segunda derivada si las ingresa.
- Usar tablas de ancho fijo con f-strings en verbose, alineadas a la izquierda:

```python
print(f"{'n':<3} | {'x_n':<20} | {'E_n':<20}")
print(f"{n:<3} | {x:<20.12g} | {error:<20.12g}")
```

- Separar el codigo en funciones: `parse_args()`, una funcion del metodo numerico, y helpers como `build_function(...)` si hacen falta.
- Al final, parsear argumentos, ejecutar el metodo e imprimir el resultado.

## Como correr los scripts nuevos

Ejemplo biseccion por iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/biseccion.py -f "x**3 - x - 2" -a 1 -b 2 -i 5 -v
```

Ejemplo biseccion por error, ignorando iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/biseccion.py -f "x**3 - x - 2" -a 1 -b 2 -e 0.001 -v
```

Ejemplo Newton por iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/newton-raphson.py -f "x**3 - x - 2" -x 1.5 -i 5 -v
```

Ejemplo Newton por error, ignorando iteraciones:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/newton-raphson.py -f "x**3 - x - 2" -x 1.5 -e 0.001 -v
```

Ejemplo Newton con derivada manual opcional:

```bash
cd /Users/rodri/ITBA/metodos
python3 1_Ecuaciones-no-lineales/newton-raphson.py -f "x**3 - x - 2" -d "3*x**2 - 1" -s "6*x" -x 1.5 -i 5 -v
```

## Archivos legacy de codigos_nash

Usar estos archivos solo cuando todavia no exista script nuevo para el metodo, o para corroborar resultados durante la migracion.

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

Los archivos de Nash suelen tener ejemplos hardcodeados en `if __name__ == "__main__"`. Normalmente conviene importar la funcion desde `python3 -c` y pasar lambdas.

Ejemplo biseccion:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/roots'); from bisection import bisection_method; bisection_method(lambda x: x**3-x-2, [1,2], 100, 1e-5)"
```

Ejemplo Newton:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/roots'); from newton_raphson import newton_raphson; newton_raphson(lambda x: x**3-x-2, lambda x: 3*x**2-1, 1.5, 100, 1e-5)"
```

Ejemplo punto fijo:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/roots'); from fixed_point import fixed_point_method; fixed_point_method(lambda x: (x+2)**(1/3), 1.5, [1,2], 100, 1e-5)"
```

Ejemplo PVI Euler/Heun/RK4:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/ivp'); from euler import euler_method; T,Y=euler_method(lambda t,y: t-y, [0,1], 3, 0.1, 10); print(T); print(Y)"
```

Para Heun cambiar `from euler import euler_method` por `from heun import heun_method`. Para RK4 usar `from runge_kutta import rk4`.

Ejemplo Taylor:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/ivp'); from taylor import taylor_second_order; taylor_second_order(lambda t,y: 1+y**2, lambda t,y: 2*y*(1+y**2), [0,1], 1, 0.2, 5)"
```

Ejemplo integracion:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/integration'); from newton_cotes import trapez_method; print(trapez_method(lambda x: math.exp(x*x), (0,3), 10))"
```

Ejemplo rectangulos:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/integration'); from rectangle import midpoint_area; print(midpoint_area(lambda x: math.sin(x), (0, math.pi), 100))"
```

Ejemplo Gauss-Legendre:

```bash
cd /Users/rodri/ITBA/metodos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/integration'); from gauss_legendre import non_equidistant_two_points; print(non_equidistant_two_points(lambda x: x**4*math.cos(x), (2,8)))"
```

## Convenciones importantes

- En punto fijo se debe ingresar `g(x)` para la iteracion `x = g(x)`, no la funcion original `f(x) = 0`.
- En PVI, si el enunciado da paso `h`, calcular `N = (b-a)/h`.
- Para ecuaciones diferenciales de segundo orden, convertir a sistema:

```text
u1 = y
u2 = y'
u1' = u2
u2' = expresion despejada de y''
```

## Cuando el enunciado tenga problemas

Si el enunciado parece inconsistente, decirlo claramente antes de dar una respuesta alternativa.

Ejemplos:

- Si una ecuacion no tiene raiz real.
- Si un despeje de punto fijo diverge.
- Si el metodo solicitado no converge con los datos dados.
- Si el codigo existente no puede representar el caso sin editar un archivo hardcodeado.
- Si un codigo usa una convencion distinta a la del enunciado.

En esos casos, explicar que se corrio, que paso, y cual seria la interpretacion alternativa mas probable solo si corresponde.

## Estilo

No llenar la respuesta con teoria innecesaria. Incluir solo la transformacion matematica necesaria para justificar que se esta ingresando la funcion correcta.

Siempre distinguir entre:

- El valor que devuelve el codigo.
- El valor final truncado.
- El valor final redondeado.
- Cual de esos valores corresponde entregar segun el enunciado.
- El valor final con coma decimal cuando tenga decimales.
