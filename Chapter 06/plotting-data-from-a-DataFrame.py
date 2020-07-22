

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng
rng = default_rng(12345)

diffs = rng.standard_normal(size=100)
walk = np.add.accumulate(diffs)
df = pd.DataFrame({
    "diffs": diffs,
    "walk": walk
})

fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)

df["walk"].plot(ax=ax1, title="Random walk")
ax1.set_xlabel("Index")
ax1.set_ylabel("Value")

df["diffs"].plot(kind="hist", ax=ax2, title="Histogram of diffs")
ax2.set_xlabel("Difference")


plt.show()
