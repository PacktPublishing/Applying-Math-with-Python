import matplotlib.pyplot as plt
import skimage
from skimage.io import imread
from skimage.feature import canny


image = imread("mandelbrot.png", as_gray=True)


edges = canny(image, sigma=0.5)

fig, ax = plt.subplots()
ax.imshow(edges, cmap="gray_r")
ax.set_axis_off()


fig.savefig("mandelbrot-edges.png", dpi=300, bbox_inches="tight", pad_inches=0)

plt.show()