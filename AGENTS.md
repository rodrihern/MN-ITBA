# Instrucciones para responder ejercicios de Metodos Numericos

Estas instrucciones aplican cuando el usuario pida resolver ejercicios de metodos numericos en este workspace.

## Objetivo de la respuesta

Cada respuesta debe incluir dos cosas:

1. La solucion del ejercicio, con el resultado final en el formato pedido por el enunciado.
2. Como reproducir ese resultado usando los codigos existentes de `codigos_nash` y, cuando aplique, `codigos_marengo`.

No crear scripts nuevos para resolver un ejercicio si un codigo existente puede usarse. Solo modificar o crear codigo si el usuario lo pide explicitamente, o si no existe ninguna forma razonable de hacerlo con los archivos existentes.

## Flujo recomendado

1. Identificar el metodo pedido y los datos del enunciado.
2. Revisar el archivo correspondiente antes de responder, porque muchas funciones tienen parametros especificos y ejemplos hardcodeados.
3. Correr el codigo localmente cuando sea posible.
4. Corroborar con `codigos_nash` y `codigos_marengo` si ambos tienen implementacion aplicable.
5. Si `codigos_marengo` no tiene ese metodo, decirlo claramente. En ese caso usar `codigos_nash` y, si sirve, corroborar con un one-liner de Octave que implemente la formula sin crear archivos.

## Formato recomendado de respuesta

Responder en espanol, directo y practico:

```text
Resultado:
<resultado final con coma decimal si tiene decimales>

codigos_nash:
<comando exacto desde /Users/rodri/ITBA/metodos/codigos>
Salida: <linea relevante>

codigos_marengo:
<comando exacto desde /Users/rodri/ITBA/metodos/codigos>
Salida: <linea relevante>

Para entregar:
```text
<solo el valor final a entregar con coma decimal si tiene decimales>
```

Es importante que este en un unico bloque de texto para que se pueda copiar solamente la respuesta

Notas:
<aclaraciones importantes, si hacen falta>
```

Usar siempre coma decimal en los resultados finales que se muestran al usuario (`0,125`, no `0.125`). Las salidas crudas de Python/Octave pueden mostrarse con punto si asi las imprime el programa, pero en `Resultado` y `Para entregar` convertir a coma decimal. Cuando el resultado final tenga una cantidad fija de decimales, mostrar tanto el valor truncado como el redondeado. Si el enunciado pide explicitamente truncar, redondear, parte entera o coma decimal, indicar cual corresponde entregar.
Al final de cada respuesta incluir un bloque fenced `text` que contenga solamente el valor final a entregar, sin etiqueta, explicacion ni unidades extra, para que el usuario pueda copiarlo y pegarlo directamente.

En la respuesta incluir:

- El comando exacto desde `/Users/rodri/ITBA/metodos/codigos`.
- Los valores exactos que hay que pasar.
- Que linea de salida contiene el valor que debe usarse.
- La limitacion concreta si algun codigo no reproduce exactamente el enunciado.

## Archivos existentes

### codigos_nash

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

### codigos_marengo

| Metodo | Archivo | Firma |
|---|---|---|
| Biseccion | `codigos_marengo/biseccion.m` | `[k,X,E] = biseccion(f,a,b,prec,maxiter)` |
| Newton | `codigos_marengo/newton.m` | `[k,X,E] = newton(f,fp,x0,prec,maxiter)` |
| Newton congelado | `codigos_marengo/newtoncongelado.m` | `[k,X,E] = newtoncongelado(f,fp,x0,prec,maxiter)` |
| Newton con grafico | `codigos_marengo/newtoncongraf.m` | `[k,X,E] = newtoncongraf(f,fp,a,b,x0,prec)` |
| Punto fijo | `codigos_marengo/puntofijo.m` | `[k,X,E] = puntofijo(g,x0,prec,maxiter)` |
| Punto fijo con grafico | `codigos_marengo/puntofijocongraf.m` | `[k,X,E] = puntofijocongraf(g,a,b,x0,prec)` |
| Euler | `codigos_marengo/euler.m` | `[T,Y] = euler(f,a,b,ya,N)` |
| Heun | `codigos_marengo/heun.m` | `[T,Y] = heun(f,a,b,ya,N)` |
| Punto medio | `codigos_marengo/puntomedio.m` | `[T,Y] = puntomedio(f,a,b,ya,N)` |
| Taylor orden 2 | `codigos_marengo/taylor2.m` | `[T,Y] = taylor2(f,fp,a,b,ya,N)` |
| Taylor orden 3 | `codigos_marengo/taylor3.m` | `[T,Y] = taylor3(f,fp,fpp,a,b,ya,N)` |
| Taylor orden 4 | `codigos_marengo/taylor4.m` | `[T,Y] = taylor4(f,fp,fpp,fppp,a,b,ya,N)` |
| RK3 | `codigos_marengo/rk3.m` | `[T,Y] = rk3(f,a,b,ya,N)` |
| RK4 | `codigos_marengo/rk4.m` | `[T,Y] = rk4(f,a,b,ya,N)` |
| Simpson compuesto | `codigos_marengo/simpsoncomp.m` | `S = simpsoncomp(f,a,b,subint)` |
| Jacobi | `codigos_marengo/jacobi.m` | `[k,X,E] = jacobi(A,Y,X0,prec,maxiter)` |
| Gauss-Seidel | `codigos_marengo/gseid.m` | `[k,X,E] = gseid(A,Y,X0,prec,maxiter)` |

## Como correr codigos_nash

Los archivos de Nash suelen tener ejemplos hardcodeados en `if __name__ == "__main__"`. Normalmente conviene importar la funcion desde `python3 -c` y pasar lambdas.

Ejemplo biseccion:

```bash
cd /Users/rodri/ITBA/metodos/codigos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/roots'); from bisection import bisection_method; bisection_method(lambda x: x**3-x-2, [1,2], 100, 1e-5)"
```

Ejemplo Newton:

```bash
cd /Users/rodri/ITBA/metodos/codigos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/roots'); from newton_raphson import newton_raphson; newton_raphson(lambda x: x**3-x-2, lambda x: 3*x**2-1, 1.5, 100, 1e-5)"
```

Ejemplo punto fijo:

```bash
cd /Users/rodri/ITBA/metodos/codigos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/roots'); from fixed_point import fixed_point_method; fixed_point_method(lambda x: (x+2)**(1/3), 1.5, [1,2], 100, 1e-5)"
```

Ejemplo PVI Euler/Heun/RK4:

```bash
cd /Users/rodri/ITBA/metodos/codigos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/ivp'); from euler import euler_method; T,Y=euler_method(lambda t,y: t-y, [0,1], 3, 0.1, 10); print(T); print(Y)"
```

Para Heun cambiar `from euler import euler_method` por `from heun import heun_method`. Para RK4 usar `from runge_kutta import rk4`.

Ejemplo Taylor:

```bash
cd /Users/rodri/ITBA/metodos/codigos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/ivp'); from taylor import taylor_second_order; taylor_second_order(lambda t,y: 1+y**2, lambda t,y: 2*y*(1+y**2), [0,1], 1, 0.2, 5)"
```

Ejemplo integracion:

```bash
cd /Users/rodri/ITBA/metodos/codigos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/integration'); from newton_cotes import trapez_method; print(trapez_method(lambda x: math.exp(x*x), (0,3), 10))"
```

Ejemplo rectangulos:

```bash
cd /Users/rodri/ITBA/metodos/codigos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/integration'); from rectangle import midpoint_area; print(midpoint_area(lambda x: math.sin(x), (0, math.pi), 100))"
```

Ejemplo Gauss-Legendre:

```bash
cd /Users/rodri/ITBA/metodos/codigos
python3 -c "import sys, math; sys.path.insert(0, 'codigos_nash/integration'); from gauss_legendre import non_equidistant_two_points; print(non_equidistant_two_points(lambda x: x**4*math.cos(x), (2,8)))"
```

## Como correr codigos_marengo

Los codigos de Marengo se corren con Octave desde `/Users/rodri/ITBA/metodos/codigos`:

```bash
cd /Users/rodri/ITBA/metodos/codigos
octave --quiet --eval "format long; addpath('codigos_marengo'); ..."
```

Ejemplo biseccion:

```bash
cd /Users/rodri/ITBA/metodos/codigos
octave --quiet --eval "format long; addpath('codigos_marengo'); [k,X,E]=biseccion(@(x) x^3-x-2, 1, 2, 1e-5, 100); disp([k, X(end), E(end)]);"
```

Ejemplo Newton:

```bash
cd /Users/rodri/ITBA/metodos/codigos
octave --quiet --eval "format long; addpath('codigos_marengo'); [k,X,E]=newton(@(x) x^3-x-2, @(x) 3*x^2-1, 1.5, 1e-5, 100); disp([k, X(end), E(end)]);"
```

Ejemplo punto fijo:

```bash
cd /Users/rodri/ITBA/metodos/codigos
octave --quiet --eval "format long; addpath('codigos_marengo'); [k,X,E]=puntofijo(@(x) (x+2)^(1/3), 1.5, 1e-5, 100); disp([k, X(end), E(end)]);"
```

Ejemplo PVI:

```bash
cd /Users/rodri/ITBA/metodos/codigos
octave --quiet --eval "format long; addpath('codigos_marengo'); [T,Y]=euler(@(t,y) t-y, 0, 1, 3, 10); disp([T(:), Y(:)]);"
```

Para Heun cambiar `euler` por `heun`. Para punto medio usar `puntomedio`. Para RK4 usar `rk4`. En Marengo, `N` es la cantidad de subintervalos; si el enunciado da paso `h`, calcular `N = (b-a)/h`.

Ejemplo Taylor:

```bash
cd /Users/rodri/ITBA/metodos/codigos
octave --quiet --eval "format long; addpath('codigos_marengo'); [T,Y]=taylor2(@(t,y) 1+y^2, @(t,y) 2*y*(1+y^2), 0, 1, 1, 5); disp([T(:), Y(:)]);"
```

Ejemplo Simpson compuesto:

```bash
cd /Users/rodri/ITBA/metodos/codigos
octave --quiet --eval "format long; addpath('codigos_marengo'); S=simpsoncomp(@(x) exp(x.^2), 0, 3, 10); disp(S);"
```

Si Marengo no tiene una funcion para el metodo pedido, no inventar un archivo nuevo. Decir que no existe implementacion en `codigos_marengo` y, si conviene para corroborar, usar un one-liner directo de Octave con la formula.

## Convenciones importantes

- En punto fijo se debe ingresar `g(x)` para la iteracion `x = g(x)`, no la funcion original `f(x) = 0`.
- En Marengo, varios metodos devuelven vectores completos. Por ejemplo, en punto fijo `X(1) = x0`, entonces `X(7)` corresponde a `x6`.
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
