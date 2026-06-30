
# Problemas de valor inicial (EDOs)

Sirven para resolver ecuaciones del tipo $y' = f(t, y)$ con $y(t_0) = y_0$ en un intervalo $[a, b]$

Ahora lo que buscamos es una funcion, que la aproximamos con una tabla de valores en un intervalo $[a, b]$ 


$$
h = \frac{b-a}{M} \iff M=\frac{b-a}{h}
$$

$M$: numero de pasos
$h$: paso (distancia entre puntos)

## Euler

### Metodo

Se parte del valor inicial y se usa la formula recursiva

$$
y_{k+1} = y_k + h \cdot f(t_k, y_k)
$$

donde 

$$
t_{k+1} = t_k + h \ con \ k = \{0, 1,...,M-1\}
$$
$$t_k = a+kh$$
### Errores

| Global               | Local                                             | Final          |
| -------------------- | ------------------------------------------------- | -------------- |
| $e_k = y(t_k) - y_k$ | $e_{k+1} = y(t_{k+1}) - y_k - h\cdot f(t_k, y_k)$ | $E=y(b) - y_m$ |
### Calculadora

1. Ingresamos el valor inicial y ponemos `=`
2. Ingresamos $ans + h\cdot f(x, ans)$  con 
3. apretamos `calc` y ponemos $x=t_k$ del renglon anterior

y los ponemos en una tabla 

| $k$ | $t_k$ | $y_k$ |
| --- | ----- | ----- |
|     |       |       |
### Ejemplo

![](attachments/Pasted%20image%2020260630160437.png)

---
## Taylor de orden 2

### Metodo

Primero derivamos $y'(t) = f(t, y)$ obteniendo $y''(t) = g(t, y)$

Ahora la formula es la siguiente

$$
y_{k+1} = y_k + h \cdot f(t_k, y_k) + \frac{h^2}{2} g(t_k, y_k)
$$

Es igual al de euler pero le agregamos el termino $\frac{h^2}{2} g(t_k, y_k)$

### Error Global
$$
E_{k+1} = O(h^2)
$$

### Calculadora

1. Ingresamos el valor inicial y ponemos `=`
2. Ingresamos $ans + h\cdot f(x, ans) + \frac{h^2}{2} g(x, ans)$   con 
3. apretamos `calc` y ponemos $x=t_k$ del renglon anterior

y los ponemos en una tabla 

| $k$ | $t_k$ | $y_k$ |
| --- | ----- | ----- |
|     |       |       |

### Ejemplo

![](attachments/Pasted%20image%2020260630163013.png)

---

## Heun orden 2

### Metodo

Partimos del valor inicial y utilizamos la formula
$$
y_{k+1} = y_k + \frac{k_1+k_2}{2}
$$
donde
- $k_1 = h \cdot f(t_k, y_k)$
- $k_2 = h \cdot f(t_{k+1}, y_k + k_1)$

### Errores

Local y global $O(h^2)$

### Calculadora

1. Ingresamos el valor inicial y le damos a `=`
2. Ponemos $$ans + h \cdot \frac{f(x, ans)}{f(x+h, ans+f(x,ans))}$$
3. apretamos `calc` y ponemos $x=t_k$ del renglon anterior

y llenamos la tabla

| $k$ | $t_k$ | $y_k$ |
| --- | ----- | ----- |
|     |       |       |
