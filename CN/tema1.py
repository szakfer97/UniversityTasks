import math

def main():
    print("Metoda Gauss-Seidel cu 3 parametrii")
    x = [0] * 100000
    y = [0] * 100000
    z = [0] * 100000
    print("x[0] = ", end="")
    x[0] = float(input())
    print("y[0] = ", end="")
    y[0] = float(input())
    print("z[0] = ", end="")
    z[0] = float(input())
    print("eps = ", end="")
    eps = float(input())
    x[1] = f(x[0], y[0], z[0])
    y[1] = g(x[0], y[0], z[0])
    z[1] = h(x[0], y[0], z[0])
    n = 1
    while abs(x[n] - x[n - 1]) >= eps or abs(y[n] - y[n - 1]) >= eps or abs(z[n] - z[n - 1]) >= eps:
        x[n + 1] = f(x[n], y[n], z[n])
        y[n + 1] = g(x[n + 1], y[n], z[n])
        z[n + 1] = h(x[n + 1], y[n + 1], z[n])
        n += 1
    print(f"n = {n}")
    print(f"x[n] = {x[n]}")
    print(f"y[n] = {y[n]}")
    print(f"z[n] = {z[n]}")
def f(x: float, y: float, z: float):
    return math.sqrt(0.5 * (y*z + 5*x -1))
def g(x: float, y: float, z: float):
    return math.sqrt(2*x + math.log(z))
def h(x: float, y: float, z: float):
    return math.sqrt(x*y + 2*z + 8)
if __name__ == "__main__":
   main()