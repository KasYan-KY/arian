import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Creează figura și axele
fig, ax = plt.subplots()

# Adaugă fundal alb
ax.add_patch(patches.Rectangle((0, 0), 6, 4, color='white'))

# Adaugă benzile albastre
ax.add_patch(patches.Rectangle((0, 3.5), 6, 0.5, color='blue'))
ax.add_patch(patches.Rectangle((0, 0), 6, 0.5, color='blue'))

# Funcție pentru a desena Steaua lui David
def draw_star_of_david(ax, center, size, color):
    # Triunghiurile
    triangle1 = np.array([
        [center[0], center[1] + size],
        [center[0] - size * np.sin(np.pi/3), center[1] - size / 2],
        [center[0] + size * np.sin(np.pi/3), center[1] - size / 2]
    ])
    triangle2 = np.array([
        [center[0], center[1] - size],
        [center[0] - size * np.sin(np.pi/3), center[1] + size / 2],
        [center[0] + size * np.sin(np.pi/3), center[1] + size / 2]
    ])
    ax.add_patch(patches.Polygon(triangle1, closed=True, edgecolor=color, facecolor='none', linewidth=3))
    ax.add_patch(patches.Polygon(triangle2, closed=True, edgecolor=color, facecolor='none', linewidth=3))

# Desenează Steaua lui David
draw_star_of_david(ax, center=(3, 2), size=1, color='blue')

# Setează limitele axelor și aspectul
ax.set_xlim(0, 6)
ax.set_ylim(0, 4)
ax.set_aspect('equal')
ax.axis('off')  # Ascunde axele

# Afișează steagul
plt.show()
