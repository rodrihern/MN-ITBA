
# Interpolacion

Dado $n$ de puntos $(x_k, y_k)$, hallar una curva que pase por esos puntos

- Si el valor se encuentra entre los puntos medidios -> INTERPOLAR
- Si el valor se encuentra fuera de ese rango -> EXTRAPOLAR

Vamos a usar polinomios para interpolar, el cual tiene esta forma
$$
y = a_{n-1} x^{n-1} + a_{n-2} x^{n-2} + \dots + a_1x + a_0
$$

>[!important] Teorema
>Si se cuenta con n puntos, existe un unico polinomio de grado n-1 que pasa por todos los n puntos. No importa por que metodo se calcule, ese polinomio interpolador **siempre** sera el mismo

## Tradicional

### Metodo

Se puede armar un sistema de ecuaciones imponiendo que el polinomio pase por cada punto $(x_k, y_k)$:

$$
\begin{cases}
y_0 = a_{n-1}x_0^{\,n-1} + a_{n-2}x_0^{\,n-2} + \dots + a_1 x_0 + a_0 \\
\;\;\vdots \\
y_{n-1} = a_{n-1}x_{n-1}^{\,n-1} + a_{n-2}x_{n-1}^{\,n-2} + \dots + a_1 x_{n-1} + a_0
\end{cases}
$$

### Calculadora

Hacemos el sistema de ecuaciones con la funcion de la calculadora para hacer sistemas de ecuaciones

---
## Polinomio de Lagrange

### Metodo

Con $n$ puntos $(x_k, y_k)$ el polinomio interpolador (grado $n-1$) se escribe como una suma ponderada:

$$
P_{n-1}(x) = \sum_{k=0}^{n-1} y_k \, L_k(x)
$$

donde cada **polinomio base** $L_k(x)$ vale $1$ en $x_k$ y $0$ en el resto de los nodos:

$$
L_k(x) = \prod_{\substack{j=0 \\ j \neq k}}^{n-1} \frac{x - x_j}{x_k - x_j}
$$

Es decir, en el numerador van todos los $(x - x_j)$ salvo el propio $x_k$, y en el denominador lo mismo pero evaluado en $x_k$.

Por ejemplo si $n=3$

$$
P_2(x) = y_0 \cdot \frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)} + y_1 \cdot \frac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)} + y_2 \cdot \frac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)}
$$

### Calculadora

Vamos despacito termino por termino armando el polinomio
### Ejemplo

Con $4$ puntos $\Rightarrow$ polinomio de grado $3$:

| $x$ | $y$ |
| --- | --- |
| $0{,}0$ | $1{,}000000$ |
| $0{,}4$ | $0{,}921061$ |
| $0{,}8$ | $0{,}696707$ |
| $1{,}2$ | $0{,}362358$ |

Reemplazando cada $y_k$ y cada $L_k(x)$ con los valores de la tabla:

$$
\begin{aligned}
P_3(x) =\ & 1 \cdot \frac{(x-0{,}4)(x-0{,}8)(x-1{,}2)}{(0-0{,}4)(0-0{,}8)(0-1{,}2)} + 0{,}921061 \cdot \frac{x(x-0{,}8)(x-1{,}2)}{0{,}4(0{,}4-0{,}8)(0{,}4-1{,}2)} \\[4pt]
+\ & 0{,}696707 \cdot \frac{x(x-0{,}4)(x-1{,}2)}{0{,}8(0{,}8-0{,}4)(0{,}8-1{,}2)} + 0{,}362358 \cdot \frac{x(x-0{,}4)(x-0{,}8)}{1{,}2(1{,}2-0{,}4)(1{,}2-0{,}8)}
\end{aligned}
$$

---

## Polinomio de Newton

### Metodo

Con $n$ puntos, el polinomio es de grado $n-1$ y tiene $n$ términos (coeficientes $a_0, \dots, a_{n-1}$):

$$
P_{n-1}(x) = a_0 + a_1(x-x_0) + a_2(x-x_0)(x-x_1) + \dots + a_{n-1}(x-x_0)(x-x_1)\cdots(x-x_{n-2})
$$

La gracia de esta forma es que **cada término agrega un punto sin tener que recalcular los anteriores**. Hay dos maneras de hallar los coeficientes $a_k$.

#### Matriz

Reemplazando $P(x_k) = y_k$ en cada punto se arma un sistema lineal. Como el término $k$ se anula en todos los nodos anteriores a $x_k$, la matriz queda **triangular inferior**:

$$
\begin{cases}
y_0 = a_0 \\
y_1 = a_0 + a_1(x_1-x_0) \\
y_2 = a_0 + a_1(x_2-x_0) + a_2(x_2-x_0)(x_2-x_1) \\
\;\;\vdots
\end{cases}
$$

Se resuelve por **sustitución hacia adelante**: $a_0$ sale de la primera ecuación, se reemplaza en la segunda para sacar $a_1$, y así sucesivamente.

#### Tabla de diferencias divididas

Armamos una tabla con columnas $DD_1, DD_2, DD_3, \dots$ (la columna de los $y$ sería $DD_0$). Cada celda de la columna $DD_j$ en la fila $i$ se calcula así:

$$
DD_j[\text{fila } i] = \frac{DD_{j-1}[\text{fila } i+1] - DD_{j-1}[\text{fila } i]}{x_{i+j} - x_i}
$$

Los coeficientes son la **fila de arriba de todo** (la primera celda de cada columna):

$$
a_0 = y_0, \quad a_1 = DD_1[\text{fila }0], \quad a_2 = DD_2[\text{fila }0], \quad a_3 = DD_3[\text{fila }0], \dots
$$

> [!TIP]
> Las dos formas dan el **mismo** polinomio (es único). La tabla de diferencias divididas es más rápida a mano y reaprovecha la cuenta si después agregás un punto nuevo.

### Calculadora

Conviene la tabla de diferencias divididas:

1. Primeras 2 columnas ponemos los $(x_k, y_k)$
2. Llenamos de izquierda a derecha cada celda con el siguiente valor (A es la matriz)
$$
A_{[i][j]} = \frac{A_{[i+1][j-1]} - A_{[i][j-1]}}{A_{[i+j][0]} - A_{[i][0]}}
$$

| $x$ | $y$ | $DD1$ | $DD2$ | $\dots$ |
| --- | --- | ----- | ----- | ------- |
|     |     |       |       |         |

### Ejemplo

Con los $4$ puntos del ejemplo de Lagrange:

| $x$     | $y$                   | $DD1$                   | $DD2$                   | $DD3$                  |
| ------- | --------------------- | ----------------------- | ----------------------- | ---------------------- |
| $0{,}0$ | $\mathbf{1{,}000000}$ | $\mathbf{-0{,}1973475}$ | $\mathbf{-0{,}4544219}$ | $\mathbf{0{,}0922396}$ |
| $0{,}4$ | $0{,}921061$          | $-0{,}5608850$          | $-0{,}3437344$          |                        |
| $0{,}8$ | $0{,}696707$          | $-0{,}8358725$          |                         |                        |
| $1{,}2$ | $0{,}362358$          |                         |                         |                        |

Cada celda combina las dos celdas de la columna anterior (misma fila y la de abajo) sobre la distancia entre los $x$ de los extremos. El denominador crece columna a columna ($0{,}4 \to 0{,}8 \to 1{,}2$) porque cada $DD$ salta una fila más:

$$
\begin{aligned}
DD_1[\text{fila }0] &= \frac{0{,}921061 - 1{,}000000}{x_1-x_0 = 0{,}4 - 0{,}0} = -0{,}1973475 \\[4pt]
DD_2[\text{fila }0] &= \frac{-0{,}560885 - (-0{,}1973475)}{x_2-x_0 = 0{,}8 - 0{,}0} = -0{,}4544219 \\[4pt]
DD_3[\text{fila }0] &= \frac{-0{,}3437344 - (-0{,}4544219)}{x_3-x_0 = 1{,}2 - 0{,}0} = 0{,}0922396
\end{aligned}
$$

Los coeficientes son la **fila de arriba de todo** (en negrita):

$$
a_0 = 1{,}000000,\quad a_1 = -0{,}1973475,\quad a_2 = -0{,}4544219,\quad a_3 = 0{,}0922396
$$

Y el polinomio queda:

$$
P_3(x) = 1 - 0{,}1973475\,(x-0) - 0{,}4544219\,(x-0)(x-0{,}4) + 0{,}0922396\,(x-0)(x-0{,}4)(x-0{,}8)
$$
