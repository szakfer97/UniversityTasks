import numpy as np
import matplotlib.pyplot as plt

def successive_approximations(f, a, b, alpha, beta, n, tol):
    t = np.linspace(a, b, n + 1)
    h = (b - a) / n
    x_prev = np.zeros_like(t)
    x_prev[0] = alpha
    x_prev[-1] = beta

    for _ in range(100):  
        x_new = np.zeros_like(t)
        x_new[0] = alpha
        x_new[-1] = beta

        for i in range(1, len(t) - 1):
            x_new[i] = (
                (x_prev[i - 1] + x_prev[i + 1]) / 2
                - h**2 * f(t[i], x_prev[i]) / 2
            )

        if np.linalg.norm(x_new - x_prev, np.inf) < tol:
            return t, x_new

        x_prev = x_new

    return t, x_prev 

f1 = lambda t, x: (3/2) * np.exp(t) + (1/3) * x
a1, b1 = 0, 1
alpha1, beta1 = 1, np.exp(1)
n1, tol1 = 100, 1e-14
t1, x1 = successive_approximations(f1, a1, b1, alpha1, beta1, n1, tol1)
x_exact1 = np.exp(t1)

plt.figure(figsize=(10, 6))
plt.plot(t1, x1, label="Aproximare succesivă", linestyle="--")
plt.plot(t1, x_exact1, label="Soluția exactă", linestyle="-")
plt.title("Problema 1: Aproximări succesive vs. Soluția exactă")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.grid()

f2 = lambda t, x: -(1/2) * np.cos(t) - (1/2) * x
a2, b2 = 0, np.pi / 4
alpha2, beta2 = 1, np.sqrt(2)/2
n2, tol2 = 100, 1e-14
t2, x2 = successive_approximations(f2, a2, b2, alpha2, beta2, n2, tol2)
x_exact2 = np.cos(t2)

plt.figure(figsize=(10, 6))
plt.plot(t2, x2, label="Aproximare succesivă", linestyle="--")
plt.plot(t2, x_exact2, label="Soluția exactă", linestyle="-")
plt.title("Problema 2: Aproximări succesive vs. Soluția exactă")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.grid()
plt.show()
