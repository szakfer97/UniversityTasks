import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def problema_cauchy(ax):
    def edo_cauchy(t, Y):
        y, yp = Y[0], Y[1] 
        ypp = (2/3)*np.exp(t) + (1/3)*y
        return [yp, ypp]

    t_span = [0, 1]
    Y0 = [1, 1] 
    t_eval = np.linspace(0, 1, 100)
    sol = solve_ivp(edo_cauchy, t_span, Y0, t_eval=t_eval)
    y_exact = np.exp(t_eval)

    ax.plot(t_eval, sol.y[0], label='Aproximare numerica')
    ax.plot(t_eval, y_exact, label='Solutie exacta e^x', linestyle='--')
    ax.set_xlabel('x')
    ax.set_ylabel('y(x)')
    ax.set_title('Problema Cauchy: Metoda Aproximatiilor Succesive')
    ax.legend()
    ax.grid()

def problema_bilocala(ax):
    def edo_bilocala(t, Y):
        x, xp, xpp, xppp = Y 
        xpppp = 23 / (t + 1)**7 + x**5
        return [xp, xpp, xppp, xpppp]

    def rezolva_bilocala():
        t_span = [0, 1]
        t_eval = np.linspace(0, 1, 100)
        Y0 = [1, -1, 0, 0] 
        sol = solve_ivp(edo_bilocala, t_span, Y0, t_eval=t_eval)
        x_exact = 1 / (t_eval + 1)

        ax.plot(t_eval, sol.y[0], label='Aproximare numerica')
        ax.plot(t_eval, x_exact, label='Solutie exacta 1/(t+1)', linestyle='--')
        ax.set_xlabel('t')
        ax.set_ylabel('x(t)')
        ax.set_title('Problema Bilocala: Metoda Functiei Green')
        ax.legend()
        ax.grid()

    rezolva_bilocala()

if __name__ == "__main__":
    print("Rezolvarea ambelor probleme...")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    problema_cauchy(axes[0])
    problema_bilocala(axes[1])

    plt.tight_layout()
    plt.show()
