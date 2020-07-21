import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.feature import canny


image = imread("mandelbrot.png", as_gray=True)


edges = canny(image, sigma=0.5)

fig, ax = plt.subplots()
ax.imshow(edges, cmap="gray_r")
ax.set_axis_off()



plt.show()