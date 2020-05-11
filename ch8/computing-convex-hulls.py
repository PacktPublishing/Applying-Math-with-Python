
from shapely.geometry import MultiPoint
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

from numpy.random import default_rng
rng = default_rng(12345)


raw_points = rng.uniform(-1.0, 1.0, size=(50, 2))


fig, ax = plt.subplots()
ax.plot(raw_points[:, 0], raw_points[:, 1], "k.")
ax.set_axis_off()

fig.savefig("points-without-hull.png", dpi=300)


points = MultiPoint(raw_points)


convex_hull = points.convex_hull

patch = mpl.patches.Polygon(convex_hull.exterior, alpha=0.5, ec="k", lw=1.2)

ax.add_patch(patch)


fig.savefig("points-with-convex-hull.png", dpi=300)

plt.show()