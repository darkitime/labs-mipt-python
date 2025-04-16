import matplotlib.pyplot as plt
from PIL import Image
import io

def read_frames(filename):
    frames = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        for i in range(0, len(lines), 2):
            x = list(map(float, lines[i].split()))
            y = list(map(float, lines[i + 1].split()))
            frames.append((x, y))
    return frames

def get_global_limits(frames):
    all_x = [val for frame in frames for val in frame[0]]
    all_y = [val for frame in frames for val in frame[1]]
    return min(all_x), max(all_x), min(all_y), max(all_y)

def generate_gif(frames, output_gif='animation.gif'):
    images = []
    xmin, xmax, ymin, ymax = get_global_limits(frames)

    for idx, (x, y) in enumerate(frames):
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(x, y, marker='o', color='blue')
        ax.set_title(f"Frame {idx}")
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
        ax.grid(True, linestyle='--', linewidth=0.5)

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        images.append(Image.open(buf))

    images[0].save(output_gif, save_all=True, append_images=images[1:], duration=500, loop=0)
    print(f"GIF {output_gif}")

frames = read_frames("2.dat")
generate_gif(frames)

