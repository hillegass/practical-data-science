import sympy
import numpy as np
import matplotlib.pyplot as plt

def descend(initial_guess, f, df_x, df_y):
    max_steps = 100
    step_size = 0.15

    guesses = np.zeros((max_steps, 3))
    guess = initial_guess.copy()
    for i in range(max_steps):

        # Note values
        guesses[i, 0] = guess[x]
        guesses[i, 1] = guess[y]
        guesses[i, 2] = f.evalf(subs=guess)
        grad_x = df_x.evalf(subs=guess)
        grad_y = df_y.evalf(subs=guess)
        guess[x] = guess[x] - step_size * grad_x
        guess[y] = guess[y] - step_size * grad_y

        if i > 0:
            distance = np.linalg.norm(guesses[i, 0:2] - guesses[i - 1, 0:2])
            if distance < 10**(-5):
                break
    return i, guesses

x, y = sympy.symbols('x y')
f = 3.0 * sympy.sin(x) * y + x**2 + y**2 + 0.25 * x

v_at_zero = f.evalf(subs={x:0, y:0})
print(f"f(0,0) = {v_at_zero}")

df_x = sympy.diff(f, x)
df_y = sympy.diff(f, y)
print(f"df/dx = {df_x}")
print(f"df/dy = {df_y}")

lin_x = np.linspace(-7, 7, 120)
lin_y = np.linspace(-7, 7, 120)
X, Y = np.meshgrid(lin_x, lin_y)
Z = 3.0 * np.sin(X) * Y + X**2 + Y**2 + 0.25 * X
fig1 = plt.figure(1, (12,12))
ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.contour(X, Y, Z, 21)
ax1.plot([-1.07117403, 0.9439074],  [1.31662556 , -1.21476033], 'go')

initial_guesses = [{x:-3, y:-6}, {x:2, y:6}]

for iguess in initial_guesses:
    i, guesses = descend(iguess, f, df_x, df_y)
    print(f"Initial guess: {iguess}, {i} iterations, solution: {guesses[i, :]}")

    # Just show first few steps
    for j in range(16):
        j_x = guesses[j, 0]
        delta_x = guesses[j+1, 0] - j_x
        j_y = guesses[j, 1]
        delta_y = guesses[j+1, 1] - j_y
        if j % 2 == 1:
            color = 'red'
        else:
            color = 'black'
        ax1.arrow(j_x, j_y, delta_x, delta_y, color=color)

    ax1.plot(guesses[0:13, 0],  guesses[0:13, 1], 'k+')

ax1.set_xlabel('x')
ax1.set_ylabel('y')

fig1.savefig('path.png')