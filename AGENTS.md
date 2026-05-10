# Instrucciones para responder ejercicios de Metodos Numericos

Estas instrucciones aplican cuando el usuario pida resolver ejercicios de metodos numericos en este workspace.

## Objetivo de la respuesta

Cada respuesta debe incluir dos cosas:

1. La solucion del ejercicio, con el resultado final en el formato pedido por el enunciado.
2. Como reproducir ese resultado usando los codigos existentes. Cuando sea razonable, corroborar el resultado con los tres conjuntos de codigos: `codigos_andy`, `codigos_nash` y `codigos_marengo`.

No crear scripts nuevos para resolver un ejercicio si ya hay un codigo existente que se puede usar. Solo modificar o crear codigo si el usuario lo pide explicitamente, o si no existe ninguna forma razonable de hacerlo con los archivos existentes.

## Fuente principal para saber que correr

Antes de explicar como correr un metodo de `codigos_andy`, revisar:

```bash
codigos_andy/docs/tutorial.md
```

Usar ese tutorial como guia principal para elegir archivo, comando y datos de entrada.

Para `codigos_nash` y `codigos_marengo`, revisar el archivo del metodo correspondiente antes de responder, porque suelen tener funciones parametrizadas y no siempre son interactivos.

## Formato recomendado de respuesta

Responder en espanol, directo y practico.

Estructura preferida:

```text
Resultado:
<resultado final>

Como correrlo:
<comando>

Que ingresar:
<inputs exactos>

Notas:
<aclaraciones importantes, si hacen falta>
```

Cuando el resultado final tenga una cantidad fija de decimales, mostrar tanto el valor truncado como el redondeado. Si el enunciado pide explicitamente truncar o redondear, indicar cual de los dos es el que corresponde entregar. Si pide coma decimal, mostrar ambos resultados con coma decimal.

## Reproducibilidad

Cuando sea posible, correr el codigo localmente para verificar el valor antes de responder. Preferir corroborar con:

1. `codigos_andy`
2. `codigos_nash`
3. `codigos_marengo`

Si alguno no puede reproducir exactamente el enunciado sin editar codigo, decirlo claramente y explicar que limitacion tiene.

En la respuesta, incluir:

- El comando exacto desde `/Users/rodri/ITBA/metodos`.
- Los valores exactos que hay que ingresar en la terminal.
- Que linea de salida del programa contiene el valor que debe usarse.

Ejemplo de comando base:

```bash
cd /Users/rodri/ITBA/metodos
python3 codigos_andy/codigos_viejos/puntos_fijos.py
```

## Uso de codigos existentes

Preferir estos archivos para `codigos_andy`:

- Biseccion: `codigos_andy/codigos_viejos/biseccion.py`
- Newton: `codigos_andy/codigos_buenos/newton.py`
- Punto fijo: `codigos_andy/codigos_viejos/puntos_fijos.py`
- PVI / Euler / Heun / Taylor / RK4: `codigos_andy/codigos_viejos/pvi.py`

Preferir estos archivos para `codigos_nash`:

- Biseccion: `codigos_nash/roots/bisection.py`
- Newton: `codigos_nash/roots/newton_raphson.py`
- Punto fijo: `codigos_nash/roots/fixed_point.py`
- PVI / Heun: `codigos_nash/ivp/heun.py`
- PVI / Taylor: `codigos_nash/ivp/taylor.py`
- PVI / Euler: `codigos_nash/ivp/euler.py`
- PVI / RK: `codigos_nash/ivp/runge_kutta.py`

Preferir estos archivos para `codigos_marengo`:

- Biseccion: `codigos_marengo/biseccion.m`
- Newton: `codigos_marengo/newton.m`
- Punto fijo: `codigos_marengo/puntofijo.m`
- PVI / Euler: `codigos_marengo/euler.m`
- PVI / Heun: `codigos_marengo/heun.m`
- PVI / Taylor orden 2: `codigos_marengo/taylor2.m`
- PVI / Taylor orden 3: `codigos_marengo/taylor3.m`
- PVI / Taylor orden 4: `codigos_marengo/taylor4.m`
- PVI / RK4: `codigos_marengo/rk4.m`

Para punto fijo, recordar que el programa pide `f(x)`, pero se debe ingresar `g(x)` en la forma:

```text
x = g(x)
```

El programa de punto fijo toma `x0` como el extremo superior `b`. Si el enunciado da `x0 = 0.5`, ingresar `b = 0.5`.

Para `codigos_marengo`, normalmente se corre con Octave:

```bash
octave --quiet --eval "format long; addpath('codigos_marengo'); ..."
```

Recordar que varios metodos de Marengo devuelven vectores completos. Por ejemplo, en punto fijo `X(1) = x0`, entonces `X(7)` corresponde a `x6`.

Para `codigos_nash`, normalmente conviene importar la funcion del metodo y pasarle lambdas desde `python3 -c`, porque muchos archivos tienen ejemplos hardcodeados en el bloque `if __name__ == "__main__"`.

## Cuando el enunciado tenga problemas

Si el enunciado parece inconsistente, decirlo claramente antes de dar una respuesta alternativa.

Ejemplos:

- Si una ecuacion no tiene raiz real.
- Si un despeje de punto fijo diverge.
- Si el metodo solicitado no converge con los datos dados.
- Si el codigo existente no puede representar el caso sin editar un archivo hardcodeado.
- Si un codigo usa una convencion distinta a la del enunciado, por ejemplo Newton de Andy elige automaticamente el extremo inicial desde un intervalo y no permite fijar directamente `x0`.

En esos casos, explicar que se corrio, que paso, y cual seria la interpretacion alternativa mas probable solo si corresponde.

## PVI y ecuaciones de orden mayor

Para ecuaciones diferenciales de segundo orden, convertir a sistema:

```text
u1 = y
u2 = y'
u1' = u2
u2' = expresion despejada de y''
```

Si se usa `codigos_andy/codigos_viejos/pvi.py`, explicar que ese archivo esta hardcodeado y que partes hay que editar:

```python
def g(t,y):
    return ...

N = ...
a = ...
b = ...
y0 = ...
point = ...
```

Si el enunciado da paso `h`, calcular:

```text
N = (b - a) / h
```

## Estilo

No llenar la respuesta con teoria innecesaria. Incluir solo la transformacion matematica necesaria para justificar que se esta ingresando la funcion correcta.

Siempre distinguir entre:

- El valor que devuelve el codigo.
- El valor final truncado.
- El valor final redondeado.
- Cual de esos valores corresponde entregar segun el enunciado.
