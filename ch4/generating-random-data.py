import numpy as np
import matplotlib.pyplot as plt

from numpy.random import default_rng
rng = default_rng(12345)  # changing seed for reproducibility

random_floats = rng.random(size=(5, 5))
# array([[0.22733602, 0.31675834, 0.79736546, 0.67625467, 0.39110955],
#        [0.33281393, 0.59830875, 0.18673419, 0.67275604, 0.94180287],
#        [0.24824571, 0.94888115, 0.66723745, 0.09589794, 0.44183967],
#        [0.88647992, 0.6974535 , 0.32647286, 0.73392816, 0.22013496],
#        [0.08159457, 0.1598956 , 0.34010018, 0.46519315, 0.26642103]])

random_ints = rng.integers(1, 20, endpoint=True, size=10)
# array([12, 17, 10, 4, 1, 3, 2, 2, 3, 12])


dist = rng.random(size=1000)


fig, ax = plt.subplots()
ax.hist(dist)
ax.set_title("Histogram of random numbers")
ax.set_xlabel("Value")
ax.set_ylabel("Density")


plt.show()


