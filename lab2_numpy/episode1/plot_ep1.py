import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# Пути к исходным изображениям
image_paths = [
    'lunar01_raw.jpg',
    'lunar02_raw.jpg',
    'lunar03_raw.jpg'
]

# Функция линейного растяжения контраста
def stretch_contrast(img_array):
    min_val = np.min(img_array)
    max_val = np.max(img_array)
    stretched = (img_array - min_val) * (255 / (max_val - min_val))
    return stretched.astype(np.uint8)

# Функция для отображения гистограмм
def plot_histograms(img_array, enhanced_img_array, title):
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.hist(img_array.flatten(), bins=50, color='gray')
    plt.title(f'{title} Original Histogram')
    plt.subplot(1, 2, 2)
    plt.hist(enhanced_img_array.flatten(), bins=50, color='blue')
    plt.title(f'{title} Enhanced Histogram')
    plt.tight_layout()
    plt.show()

# Обработка и сохранение изображений
for path in image_paths:
    # Загрузка изображения и перевод в ч/б
    img = Image.open(path).convert('L')
    img_array = np.array(img)

    # Улучшение изображения
    enhanced_img_array = stretch_contrast(img_array)

    # Отображаем гистограммы
    plot_histograms(img_array, enhanced_img_array, os.path.basename(path))

    # Сохранение улучшенного изображения
    filename = os.path.basename(path).replace('.jpg', '_enhanced.jpg')
    enhanced_img = Image.fromarray(enhanced_img_array)
    enhanced_img.save(filename)

    # Визуализация исходного и улучшенного изображения с фиксированным диапазоном яркости
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(img_array, cmap='gray', vmin=0, vmax=255)
    axes[0].set_title('Original')
    axes[0].axis('off')

    axes[1].imshow(enhanced_img_array, cmap='gray', vmin=0, vmax=255)
    axes[1].set_title('Enhanced')
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()
