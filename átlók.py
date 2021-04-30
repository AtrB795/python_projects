import numpy as np
from matplotlib.patches import Circle, Rectangle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt


def atlok(szam):
    megoldás = (szam*(szam-3))/2
    return megoldás

patches = []
for szám in range(100):
    #plt(0.1*szám, 0.1*atlok(szám))
    patches.append(plt(0.2, 0.2))
p = PatchCollection(patches, alpha=0.4)
plt.show()