import numpy as np

# Metoda lui Newton pentru primul sistem
def newton_method_1(x0, y0, epsilon=1e-4):
    def F(x, y):
        return 2 * x**3 - y**2 - 1

    def G(x, y):
        return x * y**3 - y - 4

    def dF_dx(x, y):
        return 6 * x**2

    def dF_dy(x, y):
        return -2 * y

    def dG_dx(x, y):
        return y**3

    def dG_dy(x, y):
        return 3 * x * y**2 - 1

    x, y = x0, y0

    while True:
        # Jacobian matrix
        J = np.array([[dF_dx(x, y), dF_dy(x, y)],
                      [dG_dx(x, y), dG_dy(x, y)]])
        
        # Function values
        F_val = np.array([F(x, y), G(x, y)])
        
        # Solving the linear system J * delta = -F
        delta = np.linalg.solve(J, -F_val)
        
        # Update x and y
        x, y = x + delta[0], y + delta[1]
        
        # Check for convergence
        if np.linalg.norm(delta, ord=2) < epsilon:
            break

    return x, y

# Metoda lui Newton pentru al doilea sistem
def newton_method_2(x0, y0, epsilon=1e-4, max_iterations=100):
    def F(x, y):
        return x**2 + y**2 - 10

    def G(x, y):
        if x + y <= 0:
            raise ValueError("Square root undefined for x + y <= 0")
        return np.sqrt(x + y) - 2

    def dF_dx(x, y):
        return 2 * x

    def dF_dy(x, y):
        return 2 * y

    def dG_dx(x, y):
        if x + y <= 0:
            raise ValueError("Derivative undefined for x + y <= 0")
        return 0.5 / np.sqrt(x + y)

    def dG_dy(x, y):
        if x + y <= 0:
            raise ValueError("Derivative undefined for x + y <= 0")
        return 0.5 / np.sqrt(x + y)

    x, y = x0, y0
    iteration = 0

    while iteration < max_iterations:
        try:
            if x + y <= 0:
                raise ValueError(f"Invalid x + y encountered during iteration: {x + y}")

            # Jacobian matrix
            J = np.array([[dF_dx(x, y), dF_dy(x, y)],
                          [dG_dx(x, y), dG_dy(x, y)]])
            
            # Function values
            F_val = np.array([F(x, y), G(x, y)])
            
            # Solving the linear system J * delta = -F
            delta = np.linalg.solve(J, -F_val)
            
            # Update x and y
            x, y = x + delta[0], y + delta[1]
            
            # Check for convergence
            if np.linalg.norm(delta, ord=2) < epsilon:
                return x, y

        except np.linalg.LinAlgError:
            print("Jacobian is singular, Newton's method fails.")
            return None, None
        except ValueError as e:
            print(e)
            return None, None
        
        iteration += 1

    print("Max iterations reached without convergence.")
    return None, None

# Apeluri funcții pentru primul sistem
x1, y1 = newton_method_1(1.2, 1.7)
print(f"Soluția pentru primul sistem: x = {x1:.4f}, y = {y1:.4f}")

# Apeluri funcții pentru al doilea sistem
x2a, y2a = newton_method_2(0.9, 3.1)
x2b, y2b = newton_method_2(2.9, 1.1)

if x2a is not None and y2a is not None:
    print(f"Soluția pentru al doilea sistem (punct inițial (0.9, 3.1)): x = {x2a:.4f}, y = {y2a:.4f}")
else:
    print("Metoda nu a reușit să găsească o soluție validă pentru punctul inițial (0.9, 3.1).")

if x2b is not None and y2b is not None:
    print(f"Soluția pentru al doilea sistem (punct inițial (2.9, 1.1)): x = {x2b:.4f}, y = {y2b:.4f}")
else:
    print("Metoda nu a reușit să găsească o soluție validă pentru punctul inițial (2.9, 1.1).")
