import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Creează figura și axele
fig, ax = plt.subplots()

# Adaugă banda roșie de sus
ax.add_patch(patches.Rectangle((0, 2), 6, 1, color='#9E3039'))  # Roșu leton

# Adaugă banda albă din mijloc
ax.add_patch(patches.Rectangle((0, 1), 6, 1, color='white'))

# Adaugă banda roșie de jos
ax.add_patch(patches.Rectangle((0, 0), 6, 1, color='#9E3039'))  # Roșu leton

# Setează limitele axelor și aspectul
ax.set_xlim(0, 6)
ax.set_ylim(0, 3)
ax.set_aspect('equal')
ax.axis('off')  # Ascunde axele

# Afișează steagul
plt.show()
