import matplotlib.pyplot as plt

def load_points(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        count = int(lines[0])
        coords = []
        for line in lines[1:count+1]:
            x, y = map(float, line.strip().split())
            coords.append((x, y))
    return coords

def main():
    import sys
    if len(sys.argv) != 2:
        print("Путь")
        return

    file = sys.argv[1]
    points = load_points(file)

    x = [p[0] for p in points]
    y = [p[1] for p in points]

    plt.figure(figsize=(9, 5))
    plt.scatter(x, y, color='blue', s=1, marker='o')
    plt.title(f'Точки наблюдения из файла {file}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.grid(True)

    output_file = file + '_plot.png'
    plt.savefig(output_file)
    plt.show()
    print(f'Сохранено в файл: {output_file}')

main()




