
# Interpolacion

Dado $n$ de puntos $(x_k, y_k)$, hallar una curva que pase por esos puntos

- Si el valor se encuentra entre los puntos medidios -> INTERPOLAR
- Si el valor se encuentra fuera de ese rango -> EXTRAPOLAR

Vamos a usar polinomios para interpolar

>[!important]
>Si se cuenta con n puntos, existe un unico polinomio de grado n-1 que pasa por todos los n puntos. No importa por que metodo se calcule, ese polinomio interpolador **siempre** sera el mismo

## Metodo Tradicional

### Metodo

Se cuentan con $n$ puntos, el polinomio a construir es de la forma

$$
y = a_{n-1} x^{n-1} + a_{n-2} x^{n-2} + ... + a_1x + a_0
$$

Se puede armar un sistema de ecuaciones 



