import matplotlib.pyplot as plt
import numpy as np

# Crea una sagoma cerebrale (ellisse semplificata)
theta = np.linspace(0, 2*np.pi, 300)
x_brain = 2 * np.cos(theta)
y_brain = 1.5 * np.sin(theta)

plt.figure(figsize=(7,5))
plt.fill(x_brain, y_brain, color='#e0e0e0', alpha=1, zorder=1)
plt.plot(x_brain, y_brain, color='gray', lw=2, zorder=2)

# Zone attivate (esempio: tre "punti caldi")
hotspots = [(-0.6, 0.7, 0.3), (0.8, 0.2, 0.25), (0, -0.8, 0.22)]
for x, y, size in hotspots:
    plt.scatter(x, y, s=2200*size, c='red', alpha=0.8, edgecolor='gold', linewidth=2, zorder=3)

plt.title("fMRI: Mappe di Attivazione Cerebrale (simulazione)")
plt.axis('off')
plt.tight_layout()
plt.savefig("fmri_map_attivazione.svg", format="svg")
plt.show()
