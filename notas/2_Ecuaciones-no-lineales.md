# Ecuaciones no lineales

Nuestro objetivo es hallar $f(x) = 0$

## Biseccion

### Requisitos

- f continua en un intervalo \[a, b]
- f cambia de signo $f(a) \cdot f(b) < 0$

Si ademas $f'$ tiene signo constante en el intervalo, sabemos que la raiz es unica en el intervalo (monotona)
### Metodo

Nos apalancamos del *Teorema de Bolzano* para encontrar un intervalo que contenga la raiz y vamos dividiendo este intervalo en 2 e iteramos en el intervalo que tenga el 0. Medio que le estamos haciendo una busqueda binaria al 0

$$
x_n = \frac{a_n - b_n}{2}
$$
- si $f(x_n) < 0 \rightarrow a_{n+1} = x_n$
- si $f(x_n) > 0 \rightarrow b_{n+1} = x_n$

### Error

En la iteracion $n$ el error es

$$
|Error| \le \frac{b_n - a_n}{2} = \frac{b_0 - a_0}{2^{n+1}} = \delta
$$

para calcular $n$ a partir de un $\delta$ maximo

$$
n = \lfloor \frac{ln(b_0 - a_0) - ln(\delta)}{ln(2)} \rfloor = \lfloor log_2(\frac{b_0-a_0}{\delta}) \rfloor
$$
### Calculadora

Primero cargamos en las variables de la calculadora `A` y `B` los valores de $a_0$ y $b_0$ respectivamente

luego:
1. Hacemos $\frac{A+B}{2}$ y lo guardamos en la variable `x`
2. Opcionalmente calculamos el error haciendo $\frac{B-A}{2}$
3. Hacemos $f(x)$ y
	- si $f(x) < 0$ entonces  $A \leftarrow x$
	- si $f(x) > 0$ entonces  $B \leftarrow x$
4. volvemos al paso 1. 

Terminamos cuando completamos la cantidad de pasos deseada o llegamos a la cota de error deseada

Mientras lo hacemos vamos cargando la siguiente tabla

| n   | a   | b   | x   | f(x) |
| --- | --- | --- | --- | ---- |
|     |     |     |     |      |

Podriamos agregar una columna extra para el error si quisieramos

### Ejemplo

![](attachments/Pasted%20image%2020260630132056.png)


completa y con cota de error

```
n    a           b          x_n          f(x_n)         cota error
0    1           2          1,5           0,875         0,5
1    1           1,5        1,25         -0,796875      0,25
2    1,25        1,5        1,375        -0,025390625   0,125
3    1,375       1,5        1,4375        0,4084472656  0,0625
4    1,375       1,4375     1,40625       0,1877441406  0,03125
5    1,375       1,40625    1,390625      0,0802345276  0,015625
6    1,375       1,390625   1,3828125     0,0271873474  0,0078125
7    1,375       1,3828125  1,37890625    0,0008397102  0,00390625
8    1,375       1,37890625 1,376953125  -0,0122995302  0,001953125
9    1,376953125 1,37890625 1,3779296875 -0,0057358593  0,0009765625
```


---
## Metodo de Newton

### Requisitos

- $f \in C^2 [a, b]$ (2 veces deribable y que la segunda derivada es continua)
- $f(a) \cdot f(b) < 0$
- f monotona ($f'(x) > 0 \ o \ f'(x) < 0 \  \forall x \in (a, b)$)

### Metodo

![](attachments/Pasted%20image%2020260630112822.png)

Vamos tirando rectas tangentes y estas se van a ir aproximando a la raiz buscada

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

Para elegir el $x_0$ tomamos el extremo cuyo signo coincide con la segunda derivada, osea $f(x_0) \cdot f''(x_0) > 0$

### Error

No se posee una cota para el error en funcion de n pero converge mas rapido que la biseccion

$$
E_n = |x_{n+1} - x_n|
$$

### Calculadora

1. pongo `x0` y le damos a `=`
2. cargamos $ans - \frac{f(ans)}{f'(ans)}$
3. spameamos `=` hasta terminar

y cargamos la tabla

| n   | $x_n$ |
| --- | ----- |
|     |       |

Si nos interesa el error hacemos la tabla

| n   | $x_n$ | $f(x_n)$ | $f'(x_n)$ | $E_n$ |
| --- | ----- | -------- | --------- | ----- |
|     |       |          |           |       |

>[!TIP]
>Si nos interesa un error menor a $10^{-k}$ hacemos las iteraciones hasta que los primeros k decimales no cambian

>[!TIP]
>No se si funciona siempre pero para elegir el extremo podemos elegir uno al azar y si no converge, cambiamos. Si converge rapido es que lo elegimos bien


### Ejemplo

![](attachments/Pasted%20image%2020260630134721.png)

tambien seria lo mismo si quisieramos un error de $10^{-4}$ (habian mas decimales en las respuestas)

---
## Metodo de puntos fijos

A partir de una $f(x) = 0$ despejo $x = g(x)$ y voy a buscar un punto fijo en g, el cual coincide con un 0 en f

### Requisitos

- g continua en \[a, b]
- $|g'(x)| < 1 \ \forall x \in [a,b]$   
- $g(x) \in [a, b], \ \forall x \in [a, b]$ (osea que la imagen queda contenida en el cuadrado)

### Metodo

$$
x_{n+1} = g(x_n)
$$
- si $g'(x) > 0$ converge como *escalera*
- si $g'(x) < 0$ converge como *telaraña*

![](attachments/Pasted%20image%2020260630115345.png)

>[!TIP]
Si vemos que no sale, probamos otra forma de despejar x

>[!note]
>Se puede tomar como $x_0$ cualquiera de los 2 extremos del intervalo

### Error

$$
E_n = |x_{n+1} - x_n|
$$

### Calculadora

1. Ingresamos `x0` ponemos `=`
2. cargamos $g(ans)$
3. spameamos `=` hasta terminar

y cargamos la tabla

| n   | $x_n$ |
| --- | ----- |
|     |       |

Si nos interesa el error en cada uno de los pasos, cargamos la tabla

| n   | $x_n$ | $f(x_n)$ | $f'(x_n)$ | $E_n$ |
| --- | ----- | -------- | --------- | ----- |
|     |       |          |           |       |

>[!TIP]
>Si nos interesa un error menor a $10^{-k}$ hacemos las iteraciones hasta que los primeros k decimales no cambian

### Ejemplo

![](attachments/Pasted%20image%2020260630150703.png)

---

