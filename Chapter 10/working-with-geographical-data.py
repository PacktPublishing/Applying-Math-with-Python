import geopandas
import geoplot
import matplotlib.pyplot as plt

world = geopandas.read_file(
        geopandas.datasets.get_path("naturalearth_lowres")
)

cities = geopandas.read_file(
        geopandas.datasets.get_path("naturalearth_cities")
)

fig, ax = plt.subplots()
geoplot.polyplot(world, ax=ax)


geoplot.pointplot(cities, ax=ax, fc="r", marker="2")
ax.axis((-180, 180, -90, 90))


plt.show()