import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy as sp

# === SymPy решение ===
x = sp.symbols('x')
y = sp.Function('y')

ode = sp.Eq(y(x).diff(x), -2 * y(x))
sol = sp.dsolve(ode, y(x), ics={y(0): sp.sqrt(2)})

# Преобразуем в численную функцию
f_sym = sp.lambdify(x, sol.rhs, modules=['numpy'])

# === SciPy численное решение ===
def rhs(t, y):
    return -2 * y

sol_num = solve_ivp(rhs, [0, 10], [np.sqrt(2)], t_eval=np.linspace(0, 10, 300))

# === Визуализация ===
t = sol_num.t
y_sym = f_sym(t)
y_num = sol_num.y[0]

plt.figure(figsize=(10, 4))
plt.plot(t, y_sym, label='SymPy', linewidth=2)
plt.plot(t, y_num, '--', label='SciPy', linewidth=2)
plt.title('Сравнение решений SymPy и SciPy')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('ode_solutions.png')
plt.show()

# === График разности ===
plt.figure(figsize=(10, 4))
plt.plot(t, y_sym - y_num, label='Разность SymPy - SciPy', color='red')
plt.xlabel('x')
plt.ylabel('Разность')
plt.title('Разность между SymPy и SciPy решениями')
plt.grid(True)
plt.tight_layout()
plt.savefig('ode_difference.png')
plt.show()

# Вывод символьного решения
sp.pprint(sol)
