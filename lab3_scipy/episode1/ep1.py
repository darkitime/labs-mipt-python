import sympy as sp

# Определение
rho, lam, mu = sp.symbols('rho lambda mu')

# Матрица
M = sp.Matrix([
    [0, 0,     0,     -1/rho, 0,      0,      0, 0, 0],
    [0, 0,     0,     0,     -1/rho,  0,      0, 0, 0],
    [0, 0,     0,     0,      0,     -1/rho,  0, 0, 0],
    [-(lam+2*mu), 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -mu,   0,     0, 0, 0, 0, 0, 0],
    [0, 0,    -mu,    0, 0, 0, 0, 0, 0],
    [-lam, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -lam, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -lam, 0, 0, 0, 0, 0, 0]
])

# Нахождение собственных значений
eigenvalues = M.eigenvals()

# Вывод
for val, mult in eigenvalues.items():
    sp.pprint(f"Eigenvalue: {val}, multiplicity: {mult}")
