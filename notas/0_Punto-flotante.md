---
materia: metodos
tipo: apuntes
---


# Representación de punto flotante (IEEE 754)

Cada número se escribe como notación científica en base 2:

$$
x = (-1)^{s} \cdot (1 + m) \cdot 2^{\,e - \text{bias}}
$$

- $s$: signo
- $m$: mantisa
- $e$: exponente
- $bias$: numero que se le resta al exponente

```text
 ┌───┬──────────────┬───────────────────────────┐
 │ s │        e     │             m             │
 └───┴──────────────┴───────────────────────────┘
 | 1 |    E bits    |          M bits           |
```

## Signo

$$
(-1)^{s} = \begin{cases} 1 & x>0 \;\;(s=0) \\ -1 & x<0 \;\;(s=1)\end{cases}
$$
## Exponente

Se toma como un numero binario normal. Se le resta un sesgo (*bias*) al ponerlo en el exponente

## Mantisa

Se toma como la parte decimal de un numero binario


$$
m = \sum_{k=0}^{M} m_k \, 2^{-k} = \frac{m_1}{2} + \frac{m_2}{4} + \frac{m_3}{8} + \dots + \frac{m_{M}}{2^{M}}, \qquad m \in [0,1)
$$

## Conceptos



**Epsilon**: Valor minimo que puede cambiar la mantisa $\rightarrow 2^{-M}$

**Real max**: valor maximo representable (m todos 1 y e todos 1)

**Distancia entre numeros consecutivos**: $\Delta = eps \cdot 2^{e-bias}$ 

## Comparacion

|                             | Simple (32 bits) | Doble (64 bits) | Cuadruple (128 bits) |
| --------------------------- | ---------------- | --------------- | -------------------- |
| Signo / Exponente / Mantisa | 1 / 8 / 23       | 1 / 11 / 52     | 1 / 15 / 112         |
| Sesgo (*bias*)              | $127$            | $1023$          | $16383$              |
| Epsilon ($2^{-M}$)          | $2^{-23} \approx 1{,}2\cdot10^{-7}$ | $2^{-52} \approx 2{,}2\cdot10^{-16}$ | $2^{-112} \approx 1{,}9\cdot10^{-34}$ |
| Real max                    | $\approx 3{,}4\cdot10^{38}$ | $\approx 1{,}8\cdot10^{308}$ | $\approx 1{,}2\cdot10^{4932}$ |

## Ejemplo 64 bits

Doble precisión reparte los 64 bits en **1** (signo) **+ 11** (exponente, bias $1023$) **+ 52** (mantisa):

```text
 ┌───┬──────────────┬───────────────────────────┐
 │ s │   E (11 b)   │          m (52 b)         │
 └───┴──────────────┴───────────────────────────┘
```

$$
x = (-1)^{s}\,(1+m)\,2^{\,E-1023}, \qquad E = \sum_{k=0}^{10} e_k \, 2^{k}
$$

$E$ es el entero formado por los 11 bits (de $1$ a $2046$); el exponente real $E-1023$ va de $-1022$ a $1023$:

| Bits ($E$) | $E$ | $2^{E-1023}$ | |
|---|---|---|---|
| `00000000001` | $1$ | $2^{-1022}$ | menor exponente normal |
| `01111111111` | $1023$ | $2^{0}$ | offset cero |
| `11111111110` | $2046$ | $2^{1023}$ | mayor exponente |

> [!NOTE] Reservados
> $E=0$ y $E=2047$ se usan para los **casos especiales**: $\pm 0$, subnormales, $\pm\infty$ y **NaN** ($0/0$, $\sqrt{-1}$).

> [!IMPORTANT] Valores en doble precisión
> - $\varepsilon = 2^{-52} \approx 2{,}2\cdot10^{-16}$
> - realmax $= (2-\varepsilon)\,2^{1023} \approx 1{,}8\cdot10^{308}$
> - distancia entre consecutivos: $\Delta = \varepsilon\cdot 2^{\,E-1023}$ → en $[1,2)$ vale $\varepsilon$; en $[2,4)$, $2\varepsilon$; en $[0{,}5,1)$, $\varepsilon/2$.

### Representar $-6{,}5$

1. **Signo:** $-6{,}5 < 0 \Rightarrow s = 1$.
2. **A binario:** $6{,}5 = 4 + 2 + 0{,}5 = 110{,}1_2$.
3. **Normalizar:** $110{,}1_2 = 1{,}101_2 \times 2^{2}$ → exponente real $= 2$, fracción $= 101$.
4. **Exponente almacenado:** $E = 2 + 1023 = 1025 = 10000000001_2$.
5. **Mantisa (52 bits):** la fracción $101$ rellenada con ceros → $m = 0{,}101_2 = \tfrac12 + \tfrac18 = 0{,}625$.
6. **Armado** (signo · exponente · mantisa):

```text
 s            E                              m
 1  10000000001  1010000000000000000000000000000000000000000000000000
```

En hexadecimal: `0xC01A000000000000`.

> [!TIP] Verificación
> $x = (-1)^{1}\,(1 + 0{,}625)\,2^{\,1025-1023} = -1{,}625 \cdot 4 = -6{,}5$ ✓

## Error de redondeo

Al guardar $x$, la máquina lo aproxima por el flotante más cercano $\text{fl}(x)$. El error **relativo** está acotado por la unidad de redondeo:

$$
\frac{|x - \text{fl}(x)|}{|x|} \le \frac{1}{2}\,\varepsilon_{maq}
$$

> [!NOTE] Claves
> - El error es **relativo**: los números grandes tienen huecos grandes entre representables.
> - Por eso `0.1 + 0.2 != 0.3` ($0.1$ no tiene representación binaria finita).
> - Estos errores se **acumulan y propagan** en cálculos iterativos → motivación de **estabilidad** y **condicionamiento**.
