---
materia: metodos
tipo: apuntes
---

# Algebra lineal

Resolver un sistema $A\,x = b$. Hay dos familias de métodos:

- **Directos**: eliminación gaussiana. Dan la solución **exacta** en una cantidad finita de pasos.
- **Iterativos**: Jacobi y Gauss-Seidel. **Aproximan** la solución repitiendo una fórmula; sirven para sistemas grandes y son los que más caen en los finales.

---

## Eliminación gaussiana

### Metodo

Se llevan ceros debajo de la diagonal (matriz **triangular superior**) combinando filas, y después se despeja de abajo hacia arriba (**sustitución hacia atrás**).

$$
F_i \leftarrow F_i - \frac{a_{ik}}{a_{kk}}\,F_k
$$

donde $a_{kk}$ es el **pivote**. Se opera sobre la matriz ampliada $[A \mid b]$.

### Calculadora

1. Armar la matriz ampliada $[A \mid b]$.
2. Con la fila del pivote, hacer ceros en toda la columna de abajo (regla de arriba).
3. Repetir bajando por la diagonal hasta dejarla triangular.
4. **Sustitución hacia atrás**: la última fila da una incógnita directa; se reemplaza hacia arriba.

> [!TIP]
> Si un pivote queda en $0$, hay que **intercambiar filas** (pivoteo) antes de seguir.

### Ejemplo

$$
\begin{cases}
2x + y - z = 8 \\
-3x - y + 2z = -11 \\
-2x + y + 2z = -3
\end{cases}
$$

$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & 8 \\
-3 & -1 & 2 & -11 \\
-2 & 1 & 2 & -3
\end{array}\right]
\xrightarrow{\substack{F_2 + \frac{3}{2}F_1 \\ F_3 + F_1}}
\left[\begin{array}{ccc|c}
2 & 1 & -1 & 8 \\
0 & 0{,}5 & 0{,}5 & 1 \\
0 & 2 & 1 & 5
\end{array}\right]
\xrightarrow{F_3 - 4F_2}
\left[\begin{array}{ccc|c}
2 & 1 & -1 & 8 \\
0 & 0{,}5 & 0{,}5 & 1 \\
0 & 0 & -1 & 1
\end{array}\right]
$$

Sustitución hacia atrás: $-z = 1 \Rightarrow z = -1$; luego $0{,}5y + 0{,}5(-1) = 1 \Rightarrow y = 3$; luego $2x + 3 - (-1) = 8 \Rightarrow x = 2$.

$$
(x, y, z) = (2,\ 3,\ -1)
$$

---

## Métodos iterativos

La idea común: de cada ecuación $i$ se **despeja la incógnita de la diagonal** $x_i$, y se itera a partir de un vector inicial (normalmente $x^{(0)} = 0$):

$$
x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j \neq i} a_{ij}\,x_j\right)
$$

### Requisitos (convergencia)

La sucesión converge si la matriz es **diagonalmente dominante**:

$$
|a_{ii}| \ge \sum_{j \neq i} |a_{ij}| \quad \text{en cada fila}
$$

osea que el coeficiente de la variable que estamos despejando debe "pesar" mas que todos los demas juntos

> [!TIP]
> Si no converge, a veces **reordenar las ecuaciones** (cambiar el orden de las filas) vuelve dominante la diagonal y entonces sí converge. El mismo sistema puede converger o divergir según el orden.

### Forma matricial

Descomponiendo $A = D + L + U$ (diagonal, triangular inferior y superior estrictas), cada método se escribe como:

$$
x^{(k+1)} = M\,x^{(k)} + C
$$

| Método | $M$ | $C$ |
|---|---|---|
| Jacobi | $-D^{-1}(L+U)$ | $D^{-1}b$ |
| Gauss-Seidel | $-(D+L)^{-1}U$ | $(D+L)^{-1}b$ |

El error en **norma infinito** ($\|x\|_\infty = \max_i |x_i|$) decrece en cada paso, más rápido con Gauss-Seidel que con Jacobi.

---

## Jacobi

### Metodo

Todas las incógnitas se actualizan usando **solo los valores del paso anterior** $x^{(k)}$:

$$
x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j \neq i} a_{ij}\,x_j^{(k)}\right)
$$

### Calculadora

1. Despejar cada $x_i$ de su ecuación.
2. Arrancar de $x^{(0)} = (0, \dots, 0)$.
3. Calcular **todas** las nuevas $x_i$ y las guardamos en variables
4. actualizamos las $x_i$ con las variables
5. Repetimos hasta llegar a la presicion pedida

| $k$ | $x_1$ | $x_2$ | $\dots$ |
| --- | ----- | ----- | ------- |
|     |       |       |         |

### Ejemplo

$$
\begin{cases}
2x_1 + x_2 = 8 \\
x_1 - 2x_2 = -1
\end{cases}
\Rightarrow
\begin{cases}
x_1 = \dfrac{8 - x_2}{2} \\[4pt]
x_2 = \dfrac{1 + x_1}{2}
\end{cases}
$$

Partiendo de $(0,0)$:

| $k$ | $x_1$ | $x_2$ |
| --- | ----- | ----- |
| $0$ | $0$ | $0$ |
| $1$ | $4$ | $0{,}5$ |
| $2$ | $3{,}75$ | $2{,}5$ |
| $3$ | $2{,}75$ | $2{,}375$ |

Converge a la solución $(3, 2)$. En forma matricial:

$$
M = \begin{pmatrix} 0 & -0{,}5 \\ 0{,}5 & 0 \end{pmatrix}, \qquad C = \begin{pmatrix} 4 \\ 0{,}5 \end{pmatrix}
$$

---

## Gauss-Seidel

### Metodo

Igual que Jacobi, pero cada incógnita se calcula usando **los valores ya actualizados en este mismo paso** (apenas se obtiene $x_1^{(k+1)}$ se usa para $x_2^{(k+1)}$, etc.). Por eso converge más rápido:

$$
x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j < i} a_{ij}\,x_j^{(k+1)} - \sum_{j > i} a_{ij}\,x_j^{(k)}\right)
$$

### Calculadora

Igual que Jacobi, con la diferencia clave del paso 3: En lugar de guardarlas en otras variables, actualizamos las propias $x_i$. osea que queda

1. Despejar cada $x_i$ de su ecuación.
2. Arrancar de $x^{(0)} = (0, \dots, 0)$.
3. Calcular las nuevas $x_i$ y vamos actualizando sus valores a medida que las calculamos
4. Repetimos hasta llegar a la presicion pedida

| $k$ | $x_1$ | $x_2$ | $\dots$ |
| --- | ----- | ----- | ------- |
|     |       |       |         |
### Ejemplo

Mismo sistema que en Jacobi, partiendo de $(0,0)$ (ahora $x_2$ usa el $x_1$ recién calculado):

| $k$ | $x_1$ | $x_2$ |
| --- | ----- | ----- |
| $0$ | $0$ | $0$ |
| $1$ | $4$ | $2{,}5$ |
| $2$ | $2{,}75$ | $1{,}875$ |
| $3$ | $3{,}0625$ | $2{,}03125$ |

Converge a $(3, 2)$ **más rápido** que Jacobi (compará la fila $k=3$). En forma matricial:

$$
M = \begin{pmatrix} 0 & -0{,}5 \\ 0 & -0{,}25 \end{pmatrix}, \qquad C = \begin{pmatrix} 4 \\ 2{,}5 \end{pmatrix}
$$
