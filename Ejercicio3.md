# Ejercicio 3: Resonador Bicuadrático

Diseñar un sistema de resonador bicuadrático que genere una señal:

$$
y[n] = r^n\sin[\omega_0 n]u[n]
$$

utilizando un sistema LTI de segundo orden.

a. Presente la función de transferencia.

Suponiendo que $x[n] = u[n]$, se tiene que:

$$
y[n] = h[n] = r^n\sin[\omega_0 n]u[n]
$$

entonces, utilizando la transformación:

$$
\mathcal{Z} \{(a^n \sin\omega_0 n)u[n]\} = \frac{az^{-1}\sin \omega_0}{1 - 2az^{-1}\cos \omega_0 +a^2z^{-2}}, |z| > |a|
$$

Por lo tanto, tomando en cuenta que $a = r$:

$$
H(z) = \frac{rz^{-1}\sin \omega_0}{1 - 2rz^{-1}\cos \omega_0 +r^2z^{-2}}, |z| > |r|
$$

b. Los polos y zeros se determinan despejando la función de transferencia:

$$
\frac{rz \sin}{z^2 - 2rz \cos\omega_0 + r^2}
$$

* Ceros: {0} (multiplicidad 2)
* Polos: {$r e^{-j\omega_0}$, $r e^{j\omega_0}$}


![](./img/ex3-roots.png)

c. Presente la ecuación de diferencias del sistema.

$$
Y(z) = H(z) X(z) = \frac{rz^{-1}\sin \omega_0}{1 - 2rz^{-1}\cos \omega_0 +r^2z^{-2}} X(z)
$$

$$
Y(z) \left(1 - 2rz^{-1} \cos \omega_0 + r^2z^{-2}\right) = rz^{-1} \sin \omega_0 X(z)
$$

Detransformando:

$$
y[n] - 2r\cos\omega_0 y[n-1] + r^2 y[n-2] = r\sin \omega_0x[n-1]
$$

Reordenando:

$$
y[n] = 2r\cos\omega_0 y[n-1] - r^2 y[n-2] + r\sin \omega_0x[n-1]
$$

d. Clasifique el mismo en términos de causalidad y si es FIR o IIR.

El sistema es IIR dado que:

* Depende de entradas anteriores
* Depende de salidas anteriores

e. Clasifique el mismo en términos de estabilidad para diferentes valores de r

Para que sea estable, $|r| < 1$. Suponiendo un $w_0$ y un $r = 1$

f. ¿Qué señal de entrada permite la oscilación?

Un escalón unitario, ya que el sistema oscila per se

g. ¿Qué valor de $r$ permite una oscilación (teórica) estable (constante)?

$r = 1$

h. ¿Se recomienda esta técnica para implementar osciladores digitales?

El problema de esta técnica es el factor numérico. Si $r$ es ligeramente distinto, el sistema comienza a tener divergencia o ser inestable.

i. Implemente en GNU/Octave o Python dicho sistema para F0 = 440Hz.

