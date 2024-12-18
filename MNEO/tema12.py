import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Problema 1: Cauchy - Metoda Aproximatiilor Succesive
# y'' = (2/3)e^x + (1/3)y(x), y(0)=1, y'(0)=1
# Solutia exacta: y(x) = e^x
def problema_cauchy(ax):
    # Functia pentru EDO de ordin 2 (transformata in sistem de ordin 1)
    def edo_cauchy(t, Y):
        y, yp = Y[0], Y[1]  # y = Y[0], y' = Y[1]
        ypp = (2/3)*np.exp(t) + (1/3)*y  # y''
        return [yp, ypp]

    # Conditiile initiale
    t_span = [0, 1]
    Y0 = [1, 1]  # y(0)=1, y'(0)=1
    t_eval = np.linspace(0, 1, 100)

    # Rezolvare numerica folosind solve_ivp
    sol = solve_ivp(edo_cauchy, t_span, Y0, t_eval=t_eval)

    # Solutia exacta pentru comparatie
    y_exact = np.exp(t_eval)

    # Afisare rezultate pe axa furnizata
    ax.plot(t_eval, sol.y[0], label='Aproximare numerica')
    ax.plot(t_eval, y_exact, label='Solutie exacta e^x', linestyle='--')
    ax.set_xlabel('x')
    ax.set_ylabel('y(x)')
    ax.set_title('Problema Cauchy: Metoda Aproximatiilor Succesive')
    ax.legend()
    ax.grid()


# Problema 2: Bilocala - Metoda Functiei Green
# x^{IV}(t) = 23/(t+1)^7 + x(t)^5, x(0)=1, x(1)=1/2, x'(0)=-1, x'(1)=-1/4
def problema_bilocala(ax):
    # Functia pentru rezolvarea problemei bilocale
    def edo_bilocala(t, Y):
        x, xp, xpp, xppp = Y  # x, x', x'', x'''
        xpppp = 23 / (t + 1)**7 + x**5  # x^{IV}
        return [xp, xpp, xppp, xpppp]

    # Functie de rezolvare numerica pentru problema bilocala
    def rezolva_bilocala():
        t_span = [0, 1]
        t_eval = np.linspace(0, 1, 100)

        # Conditiile initiale aproximative (cu ajustare pentru bilocale)
        Y0 = [1, -1, 0, 0]  # x(0)=1, x'(0)=-1

        # Rezolvare initiala EDO cu 4 variabile
        sol = solve_ivp(edo_bilocala, t_span, Y0, t_eval=t_eval)

        # Functia solutiei exacte pentru comparatie
        x_exact = 1 / (t_eval + 1)

        # Afisare rezultate pe axa furnizata
        ax.plot(t_eval, sol.y[0], label='Aproximare numerica')
        ax.plot(t_eval, x_exact, label='Solutie exacta 1/(t+1)', linestyle='--')
        ax.set_xlabel('t')
        ax.set_ylabel('x(t)')
        ax.set_title('Problema Bilocala: Metoda Functiei Green')
        ax.legend()
        ax.grid()

    rezolva_bilocala()


# Apelarea functiilor pentru rezolvarea problemelor
if __name__ == "__main__":
    print("Rezolvarea ambelor probleme...")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    problema_cauchy(axes[0])
    problema_bilocala(axes[1])

    plt.tight_layout()
    plt.show()
