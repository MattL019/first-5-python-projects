# Prompt: Generate a sine vs cosine curve using 'numpy', and use 'matplotlib' to draw the curve.
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = np.arange(-4*np.pi, 4*np.pi, 0.05)
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))

ax.set(xlabel='bottom', ylabel='left', title="Test graph")
ax.grid()

fig.savefig("test.png")
plt.show()

"""
Things I learned from this project:
- x, y = tuple - variable assignment via deconstructing tuples
- Practice reading library documentation
"""