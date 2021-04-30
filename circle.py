import numpy as np
from matplotlib.patches import Circle, Rectangle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


fig, ax = plt.subplots()

resolution = 50  # the number of vertices
N = 3
x = 10*np.random.rand(N)
y = 10*np.random.rand(N)
radii = 10*np.random.rand(N)
patches = []
for x1, y1, r in zip(x, y, radii):
    circle = Circle((x1, y1), r)
    patches.append(circle)
    patches.append(Rectangle((0.2, 0.2), 0.4, 0.5))

#colors = 100 * np.random.rand(len(patches))
p = PatchCollection(patches, alpha=0.4)
#p.set_array(red)
#ax.add_collection(p)
fig.colorbar(p, ax=ax)

plt.show()