# Ejercicio 4

Calcular la transformada inversa o directa de:

a. $x[n] = \{3, 0, 0, 0, 0, \underset{\uparrow}{6}, 1, 4\}$

$$
X(z) = 3 z^5 + 6 + z^{-1} + 4^{4}
$$

b. $x[n] = \left(\frac{1}{2}\right)^n, n \ge 5$

$$
X(z) = \sum_{k = 5}^{n} \left(\frac{1}{2}\right)z^{-k}
$$

c. Transformada de:

$$
H(z) = \frac{1}{(1-2z^{-1})(1-z^{-1})^2} \\
= \frac{1}{1}
$$

Por fracciones parciales:

$$
H(z) = \frac{4}{1-2z^{-1}} + \frac{-3}{1-z^{-1}} + \frac{z^{-1}}{(1-z^{-1})^2}
$$

Convirtiendo:

$$
h[n] = 4 \times 2^nu[n] - 3 u[n] + nu[n]
$$

d. $x[n] = r^n \sin(\omega_0 n)u[n]$

Por la tabla:

$$
X(z) = \frac{r z^{-1} \sin \omega_0}{1-2r z^{-1} \cos\omega_0 + r^2z^{-2}}, |z| > |a|
$$
