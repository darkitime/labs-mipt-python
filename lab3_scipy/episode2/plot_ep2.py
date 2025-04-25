import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Загрузка системы уравнений из файла
def load_system(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    N = int(lines[0])
    A = np.array([[float(num) for num in line.split()] for line in lines[1:N+1]])
    b = np.array([float(num) for num in lines[N+1].split()])
    return A, b

# Решение и визуализация
def solve_and_plot(file_path):
    A, b = load_system(file_path)
    x = np.linalg.solve(A, b)

    # Визуализация
    plt.figure(figsize=(8, 4))
    plt.bar(range(len(x)), x)
    plt.xlabel('Index')
    plt.ylabel('x[i]')
    plt.title(f'Solution of {Path(file_path).name}')
    plt.grid(True)
    plt.tight_layout()

    # Сохранение
    output_file = Path(file_path).stem + '_solution.png'
    plt.savefig(output_file)
    plt.show()

# Проверка на двух файлах
solve_and_plot('2_small.txt')
solve_and_plot('2_large.txt')