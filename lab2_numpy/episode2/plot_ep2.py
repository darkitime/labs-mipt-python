import numpy as np
import matplotlib.pyplot as plt
import os

# Пути к файлам сигналов
signal_files = [
    'signal01.dat',
    'signal02.dat',
    'signal03.dat'
]

# Скользящее среднее назад во времени (ширина окна 10) изменил
def smooth_signal(data, window=10):
    kernel = np.ones(window) / window
    return np.convolve(data, kernel, mode='full')[:len(data)]

# Обработка всех сигналов
for file in signal_files:
    # Загрузка данных
    data = np.loadtxt(file)
    smoothed = smooth_signal(data)

    # Визуализация
    plt.figure(figsize=(10, 4))
    plt.plot(data, label='Original', alpha=0.5)
    plt.plot(smoothed, label='Smoothed', linewidth=2)
    plt.title(f'Signal from {file}')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Сохранение изображения
    output_image = file.replace('.dat', '_plot.png')
    plt.savefig(output_image)
    plt.show()

