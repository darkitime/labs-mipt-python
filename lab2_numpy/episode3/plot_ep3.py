import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Загрузка начального состояния
u0 = np.loadtxt('3.dat')
N = len(u0)
T = 255

# Построение матрицы A
A = np.eye(N)
for i in range(1, N):
    A[i, i-1] = -1
A[0, -1] = -1  # циклический сдвиг

# Эволюция u во времени
U = np.zeros((T+1, N))
U[0] = u0
for n in range(T):
    U[n+1] = U[n] - 0.5 * A @ U[n]

# Визуализация как тепловая карта
plt.figure(figsize=(10, 6))
plt.imshow(U, aspect='auto', cmap='hot', origin='lower')
plt.colorbar(label='u value')
plt.xlabel('Space index')
plt.ylabel('Time step')
plt.title('Evolution of u over time')
plt.tight_layout()
plt.savefig('evolution_heatmap.png')
plt.show()

# Анимация
fig, ax = plt.subplots()
line, = ax.plot(U[0])
ax.set_ylim(np.min(U), np.max(U))
ax.set_title('u evolution over time')
ax.set_xlabel('Space index')
ax.set_ylabel('u value')

def update(frame):
    line.set_ydata(U[frame])
    ax.set_title(f'u evolution at step {frame}')
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(T+1), blit=True, interval=50)
ani.save('evolution_animation.gif', writer='pillow')
plt.show()
