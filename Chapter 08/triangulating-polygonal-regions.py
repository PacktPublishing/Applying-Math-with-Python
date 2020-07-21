import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from shapely.geometry import Polygon
from shapely.ops import triangulate

polygon = Polygon(
    [(2.0, 1.0), (2.0, 1.5), (-4.0, 1.5), (-4.0, 0.5), (-3.0, -1.5),
     (0.0, -1.5), (1.0, -2.0), (1.0, -0.5), (0.0, -1.0), (-0.5, -1.0),
     (-0.5, 1.0)],
    holes=[np.array([[-1.5, -0.5], [-1.5, 0.5], [-2.5, 0.5], [-2.5, -0.5]])]
)

fig, ax = plt.subplots()
plt_poly = mpl.patches.Polygon(polygon.exterior, ec="k", lw="1", alpha=0.5, zorder=0)
ax.add_patch(plt_poly)
plt_hole = mpl.patches.Polygon(polygon.interiors[0], ec="k", fc="w")
ax.add_patch(plt_hole)
ax.set(xlim=(-4.05, 2.05), ylim=(-2.05, 1.55))
ax.set_axis_off()


triangles = triangulate(polygon)

filtered = filter(lambda p: polygon.contains(p), triangles)

patches = map(lambda p: mpl.patches.Polygon(p.exterior), filtered)
col = mpl.collections.PatchCollection(patches, fc="none", ec="k")

ax.add_collection(col)


plt.show()
