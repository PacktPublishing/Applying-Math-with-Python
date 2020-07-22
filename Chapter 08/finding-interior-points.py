import matplotlib as mpl
import matplotlib.pyplot as plt

from shapely.geometry import Polygon, Point

polygon = Polygon(
    [(0, 2), (-1, 1), (-0.5, -1), (0.5, -1), (1, 1)],
)

fig, ax = plt.subplots()
poly_patch = mpl.patches.Polygon(polygon.exterior, ec="k", lw="1", alpha=0.5)
ax.add_patch(poly_patch)
ax.set(xlim=(-1.05, 1.05), ylim=(-1.05, 2.05))
ax.set_axis_off()


p1 = Point(0.0, 0.0)
p2 = Point(-1.0, -0.75)

ax.plot(0.0, 0.0, "k*")
ax.annotate("p1", (0.0, 0.0), (0.05, 0.0))
ax.plot(-0.8, -0.75, "k*")
ax.annotate("p2", (-0.8, -0.75), (-0.8 + 0.05, -0.75))

plt.show()

print("p1 inside polygon?", polygon.contains(p1))
print("p2 inside polygon?", polygon.contains(p2))



