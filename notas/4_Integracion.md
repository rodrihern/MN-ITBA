---
materia: metodos
tipo: apuntes
---

# Integracion numerica

Aproximar $\displaystyle I = \int_a^b f(x)\,dx$ cuando no se puede (o no conviene) integrar a mano. Se escribe:

$$
\int_a^b f(x)\,dx = \underbrace{Q[f]}_{\text{cuadratura}} + \underbrace{E[f]}_{\text{error}}
$$

La idea es integrar un **polinomio que aproxima** a $f$. Dos familias según dónde se toman los nodos:

- **Newton-Cotes**: nodos **equiespaciados** ($x_{k+1}-x_k = h$). Ej: rectángulo, trapecio, Simpson, Boole.
- **Gauss**: nodos **elegidos** para maximizar la precisión (no equiespaciados).

Para mejorar la aproximación se **aumenta el número de puntos**: se divide $[a,b]$ en $n$ subintervalos ($h=\tfrac{b-a}{n}$) y se aplica una regla simple en cada tramo → **cuadratura compuesta** (es lo que más se usa).

---

## Orden de precisión M


$M$ = **máximo grado de polinomio para el cual la fórmula es exacta** ($E[f]=0$). Se verifica integrando $1, x, x^2, \dots$ hasta que la fórmula deje de dar el valor exacto.

| Método | Orden de precisión |
|---|---|
| Newton-Cotes con $N$ impar | $M = N$ |
| Newton-Cotes con $N$ par | $M = N-1$ |
| Gauss de $N$ puntos | $M = 2N-1$ |

> [!TIP]
> En finales piden: "hallar $a, b, c, \dots$ que **maximizan el orden de precisión** de esta fórmula". Se plantea que sea exacta para $f(x)=1, x, x^2, \dots$ (una ecuación por cada uno) y se resuelve el sistema.

---

## Rectángulo

![Regla del rectangulo](https://www.youtube.com/watch?v=8zv48c0r0nQ)

### Metodo

Aproxima $f$ por una **constante** en cada tramo (la altura de un rectángulo). Hay tres variantes según qué punto se use como altura.

**Regla simple** (una sola evaluación sobre todo $[a,b]$):

$$
\begin{aligned}
\text{Izquierda:}\quad & I \approx (b-a)\,f(a) & (M=0)\\
\text{Derecha:}\quad & I \approx (b-a)\,f(b) & (M=0)\\
\text{Punto medio (= Gauss 1 punto):}\quad & I \approx (b-a)\,f\!\left(\tfrac{a+b}{2}\right) & (M=1)
\end{aligned}
$$

**Compuesta**, sobre $[a,b]$ partido en $n$ subintervalos ($h=\tfrac{b-a}{n}$):

$$
\begin{aligned}
\text{Izquierda:}\quad & I \approx h\sum_{k=0}^{n-1} f(x_k) \\
\text{Derecha:}\quad & I \approx h\sum_{k=0}^{n-1} f(x_{k+1}) \\
\text{Punto medio:}\quad & I \approx h\sum_{k=0}^{n-1} f\!\left(\tfrac{x_k+x_{k+1}}{2}\right)
\end{aligned}
$$

El **punto medio** es el más preciso de los tres (es la regla de Gauss de 1 punto, $M=1$) y su error es $|I - M_n| = \tfrac{b-a}{24}\,h^2\,|f''(\xi)|$.

### Calculadora

1. Calcular $h=\tfrac{b-a}{n}$ y los nodos $x_k = a+k\,h$.
2. Evaluar $f$ en el punto que corresponda (extremo izquierdo, derecho o medio de cada tramo).
3. Sumar todo y multiplicar por $h$.

| $k$ | $x$ | $f(x)$ |
| --- | --- | ------ |
|     |     |        |

y al final hacer la suma

### Ejemplo

$\displaystyle\int_0^1 e^x\,dx$ con $n=4$ ($h=0{,}25$), exacto $= e-1 \approx 1{,}71828$:

- **Izquierda:** $\approx 1{,}51244$
- **Derecha:** $\approx 1{,}94201$
- **Punto medio:** $\approx 1{,}71382$ (el que más se acerca)

---

## Trapecio

![](https://www.youtube.com/watch?v=rREhW5wjkUI)

### Metodo

Aproxima $f$ por una recta en cada tramo.

**Regla simple** ($M=1$):

$$
T[f] = \tfrac{b-a}{2}\big(f(a)+f(b)\big)
$$

**Compuesta**, sobre $[a,b]$ partido en $n$ subintervalos:

$$
T_n[f] = \frac{h}{2}\Big(\underbrace{f(a)+f(b)}_{E} + 2\underbrace{\textstyle\sum_{k=1}^{n-1} f(x_k)}_{\text{internos}}\Big), \qquad |I - T_n| = \frac{b-a}{12}\,h^2\,|f''(\xi)|
$$

### Calculadora

1. Calcular $h=\tfrac{b-a}{n}$ y los nodos $x_k = a+k\,h$.
2. Armar la tabla de $x_k$ y $f(x_k)$.
3. Sumar: extremos con peso $1$, internos con peso $2$.
4. Multiplicar por $\tfrac{h}{2}$.

| $k$ | $x_k$ | $f(x_k)$ |
| --- | ----- | -------- |
|     |       |          |

y al final hacer la suma
### Ejemplo

$\displaystyle\int_2^4 \ln(x+2)\,dx$ con $n=4$ ($h=0{,}5$):

| $x_k$ | $2$ | $2{,}5$ | $3$ | $3{,}5$ | $4$ |
| --- | --- | --- | --- | --- | --- |
| $f(x_k)$ | $1{,}3863$ | $1{,}5041$ | $1{,}6094$ | $1{,}7047$ | $1{,}7918$ |

$$
T_4 = \frac{0{,}5}{2}\big(1{,}3863 + 1{,}7918 + 2(1{,}5041+1{,}6094+1{,}7047)\big) \approx 3{,}2036
$$

---

## Simpson

![](https://www.youtube.com/watch?v=ypaNlJTPf9c)

### Metodo

Aproxima $f$ por parábolas.

**Regla simple** — Simpson 1/3 ($M=3$):

$$
S[f] = \tfrac{b-a}{6}\big(f(a)+4f(\tfrac{a+b}{2})+f(b)\big)
$$

> [!NOTE] Simpson = trapecio + punto medio
> $$I_S = \tfrac{1}{3}\,I_T + \tfrac{2}{3}\,I_{PM}$$

Variantes de más puntos (casi no se toman; están por completitud):

- **Simpson 3/8** ($M=3$): $\tfrac{b-a}{8}\big(f(a)+3f(x_1)+3f(x_2)+f(b)\big)$
- **Boole** ($M=5$): $\tfrac{b-a}{90}\big(7f(a)+32f(x_1)+12f(x_2)+32f(x_3)+7f(b)\big)$

**Compuesta**. Necesita $n$ **par**. Separando los internos en índices impares y pares:

Tenemos el intervalo $[x_0, x_n]$ con los $x_k$ itnermedios con $1 \le k \le n-1$
$$
A = \frac{h}{3}\Big(f(x_0) + 4\textstyle\sum_{\text{impares}} f(x_k) + 2\textstyle\sum_{\text{pares}} f(x_k)+ f(x_n)\Big)
$$
Para 6 puntos queda
$$
A = \frac{h}{3}\Big( f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + 2f(x_4) + 4f(x_5) + f(x_6) \Big)
$$


### Calculadora

1. Calcular $h=\tfrac{b-a}{n}$ ($n$ par).
2. Armar la tabla de $x_k$ y $f(x_k)$.
3. Multiplicar por $\tfrac{h}{3}$.

| $k$ | $x_k$ | $f(x_k)$ |
| --- | ----- | -------- |
|     |       |          |
y al final hacer la suma
### Ejemplo

$\displaystyle\int_0^1 t^2 e^{-t^2}\,dt$ con $n=4$ ($h=0{,}25$):

| $x_k$ | $0$ | $0{,}25$ | $0{,}5$ | $0{,}75$ | $1$ |
| --- | --- | --- | --- | --- | --- |
| $f(x_k)$ | $0$ | $0{,}0587$ | $0{,}1947$ | $0{,}3205$ | $0{,}3679$ |

$$
E = 0 + 0{,}3679, \quad IM = f(0{,}25)+f(0{,}75) = 0{,}3792, \quad P = f(0{,}5) = 0{,}1947
$$

$$
S_4 = \frac{0{,}25}{3}\big(0{,}3679 + 4\cdot 0{,}3792 + 2\cdot 0{,}1947\big) \approx 0{,}1895
$$

---

## Cuadratura de Gauss

### Metodo

En vez de nodos equiespaciados, se ubican en puntos especiales que dan **mucha más precisión con los mismos puntos** ($M = 2N-1$).

**2 puntos** ($M=3$):

$$
I \approx \frac{b-a}{2}\big(f(x_0)+f(x_1)\big), \qquad x_{0,1} = \frac{a+b}{2} \mp \frac{1}{\sqrt{3}}\cdot\frac{b-a}{2}
$$

**3 puntos** ($M=5$, mejor que Simpson):

$$
I \approx \frac{b-a}{18}\big(5f(x_0)+8f(x_1)+5f(x_2)\big), \quad x_0 = \tfrac{a+b}{2}-\sqrt{\tfrac{3}{5}}\tfrac{b-a}{2},\ \ x_1=\tfrac{a+b}{2},\ \ x_2=\tfrac{a+b}{2}+\sqrt{\tfrac{3}{5}}\tfrac{b-a}{2}
$$

### Calculadora

1. Calcular los nodos $x_i$ con las fórmulas de arriba.
2. Evaluar $f$ en cada nodo.
3. Combinar con los pesos ($1,1$ para 2 puntos; $5,8,5$ sobre $18$ para 3 puntos).

### Ejemplo

$\displaystyle\int_0^1 e^x\,dx$ (exacto $= e-1 \approx 1{,}718282$):

- **2 puntos:** $x_0=0{,}21132$, $x_1=0{,}78868$ → $I \approx \tfrac{1}{2}(e^{x_0}+e^{x_1}) \approx 1{,}717896$
- **3 puntos:** $I \approx 1{,}718281$ (¡5 puntos exactos con solo 3 evaluaciones!)

---


## Cuántos subintervalos necesito (cota de error)

### Metodo

Es lo que **más cae en finales**: dado un error máximo, hallar $n$. Se parte de la cota, se acota la derivada por su máximo en $[a,b]$, y se despeja $n$.

- **Trapecio**: error $\propto h^2$ → despejar de $\dfrac{b-a}{12}h^2\,M_2 < \text{tol}$, con $M_2 = \max|f''|$.
- **Simpson**: error $\propto h^4$ (converge mucho más rápido) → despejar de $\dfrac{b-a}{180}h^4\,M_4 < \text{tol}$, con $M_4 = \max|f^{(4)}|$. Redondear $n$ hacia arriba **al primer par**.

### Ejemplo

$\displaystyle\int_2^4 \ln(x+2)\,dx$ con Trapecio, error $< 10^{-3}$. Como $f''(x) = -\tfrac{1}{(x+2)^2}$, su máximo en valor absoluto en $[2,4]$ es $\tfrac{1}{16}$ (en $x=2$). Con $h=\tfrac{2}{n}$:

$$
|I - T_n| \le \frac{2}{12}\left(\frac{2}{n}\right)^2\frac{1}{16} = \frac{1}{24\,n^2} < 10^{-3} \ \Rightarrow\ n^2 > 41{,}7 \ \Rightarrow\ n \ge 7 \text{ subintervalos}
$$
