# Instrucciones para Metodos Numericos

Estas instrucciones aplican en `/Users/rodri/ITBA/metodos` cuando el usuario pida resolver ejercicios o editar scripts de metodos numericos.

## Prioridades

1. Para resolver ejercicios, usar el script del tema correspondiente.
2. Cuando se cree o edite codigo, seguir las convenciones de este archivo.

No crear scripts nuevos para resolver un ejercicio si ya hay una forma razonable de hacerlo con los scripts existentes. Crear o modificar codigo solo si el usuario lo pide, o si no hay forma razonable de resolver el caso con lo existente.

## Scripts

Los scripts se corren desde `/Users/rodri/ITBA/metodos`.

| Metodo | Archivo | Funcion del metodo | Argumentos principales |
|---|---|---|---|
| Biseccion | `1_Ecuaciones-no-lineales/biseccion.py` | `bisection_method` | `-f`, `-a`, `-b`, `-i`, `-e`, `-v` |
| Newton | `1_Ecuaciones-no-lineales/newton-raphson.py` | `newton_raphson_method` | `-f`, `-d`, `-s`, `-x`, `-a`, `-b`, `-i`, `-e`, `-v` |
| Punto fijo | `1_Ecuaciones-no-lineales/punto_fijo.py` | `fixed_point_method` | `-f`, `-x`, `-a`, `-b`, `-i`, `-e`, `-v` |
| Euler | `2_edos-pvi/euler.py` | `euler_method` | `-f`, `-a`, `-b`, `-y`, `-H`, `-i`, `-v` |
| Heun orden 2 | `2_edos-pvi/heun2.py` | `heun2_method` | `-f`, `-a`, `-b`, `-y`, `-H`, `-i`, `-v` |
| Taylor orden 2 | `2_edos-pvi/taylor2.py` | `taylor2_method` | `-f`, `-d`, `-a`, `-b`, `-y`, `-H`, `-i`, `-v` |
| Runge-Kutta orden 4 | `2_edos-pvi/runge-kutta4.py` | `runge_kutta4_method` | `-f`, `-a`, `-b`, `-y`, `-H`, `-i`, `-v` |
| Interpolacion Lagrange | `3_interpolacion/lagrange.py` | `lagrange_method` | `-x`, `-y`, `-p`, `-e`, `-v` |
| Interpolacion Newton | `3_interpolacion/newton.py` | `newton_method` | `-x`, `-y`, `-p`, `-e`, `-v` |
| Rectangulo | `4_integracion/rectangulo.py` | `rectangle_method` | `-f`, `-a`, `-b`, `-n`, `-m`, `-v` |
| Trapecio | `4_integracion/trapecio.py` | `trapezoid_method` | `-f`, `-a`, `-b`, `-n`, `-v` |
| Simpson 1/3 | `4_integracion/simpson.py` | `simpson_method` | `-f`, `-a`, `-b`, `-n`, `-v` |
| Gauss-Legendre | `4_integracion/gauss_legendre.py` | `gauss_legendre_method` | `-f`, `-a`, `-b`, `-p`, `-n`, `-v` |
| Eliminacion gaussiana | `5_sistemas-de-ecuaciones/eliminacion_gaussiana.py` | `gaussian_elimination_method` | `-A`, `-b`, `-v` |
| Jacobi | `5_sistemas-de-ecuaciones/jacobi.py` | `jacobi_method` | `-A`, `-b`, `-x`, `-i`, `-e`, `--matrix-form`, `-v` |
| Gauss-Seidel | `5_sistemas-de-ecuaciones/gauss-seidel.py` | `gauss_seidel_method` | `-A`, `-b`, `-x`, `-i`, `-e`, `--matrix-form`, `-v` |

## Convenciones para codigo nuevo

Todo script nuevo debe seguir este formato:

- Usar `argparse` para argumentos CLI.
- Ordenar el archivo siempre igual, de arriba hacia abajo:
  1. `import`s.
  2. Parametros editables (defaults).
  3. La funcion del metodo numerico (lo primero despues de los defaults).
  4. Helpers locales y `parse_args()`.
  5. Parseo de argumentos y llamado a la funcion del metodo.
- Definir parametros editables arriba del archivo en mayusculas, por ejemplo `A`, `B`, `X0`, `Y0`, `H`, `ITERATIONS`, `ERROR`, `FUNCTION`.
- Usar esos parametros como defaults de `argparse`, para que el script funcione tanto editando el archivo como pasando argumentos.
- La funcion del metodo se nombra como el archivo pero en ingles y con sufijo `_method`, por ejemplo `biseccion.py` -> `bisection_method`, `punto_fijo.py` -> `fixed_point_method`, `trapecio.py` -> `trapezoid_method`. Si el nombre del archivo lleva numero de orden, mantenerlo (`heun2.py` -> `heun2_method`).
- Separar el codigo en funciones: la funcion del metodo numerico, `parse_args()`, y helpers como `build_function(...)` o `build_functions(...)` si hacen falta. Como Python resuelve nombres al momento de la llamada, los helpers pueden ir despues de la funcion del metodo aunque esta los use.
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

## Verificacion de codigo nuevo

Despues de crear o editar un script, verificarlo antes de terminar.

Checklist minimo:

- Correr al menos un caso comparable con el script y confirmar que el valor final es razonable.
- Comparar el error reportado cuando aplique.
- Probar `-v` / `--verbose` y confirmar que la tabla se imprime bien.
- Probar sin `-v` y confirmar que imprime solo el resultado final.
- Probar modo por iteraciones.
- Probar modo por error/tolerancia, confirmando que ignora iteraciones.
- Probar al menos un error de entrada importante del metodo y confirmar que el script muestra un mensaje corto sin traceback.

## Como correr los scripts

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

## Flujo para resolver ejercicios

1. Identificar el metodo pedido y los datos del enunciado.
2. Revisar el script correspondiente antes de responder.
3. Correr el codigo localmente cuando sea posible.
4. Resolver con el script y explicar como correrlo.

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

## Cuando el enunciado tenga problemas

Si el enunciado parece inconsistente, decirlo claramente antes de dar una respuesta alternativa.

Ejemplos:

- Si una ecuacion no tiene raiz real.
- Si un despeje de punto fijo diverge.
- Si el metodo solicitado no converge con los datos dados.
- Si el codigo existente no puede representar el caso sin editar un archivo hardcodeado.

En esos casos, explicar que se corrio, que paso, y cual es la interpretacion o correccion mas probable solo si corresponde.

## Estilo

No llenar la respuesta con teoria innecesaria. Incluir solo la transformacion matematica necesaria para justificar que se esta ingresando la funcion correcta.

Siempre distinguir entre:

- El valor que devuelve el codigo.
- El valor final truncado.
- El valor final redondeado.
- Cual de esos valores corresponde entregar segun el enunciado.
- El valor final con coma decimal cuando tenga decimales.
