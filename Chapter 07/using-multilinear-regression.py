import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

from numpy.random import default_rng
rng = default_rng(12345)


p_vars = pd.DataFrame({
    "const": np.ones((100,)),
    "X1": rng.uniform(0, 15, size=100),
    "X2": rng.uniform(0, 25, size=100),
    "X3": rng.uniform(5, 25, size=100)
})

residuals = rng.normal(0.0, 12.0, size=100)
Y = -10.0 + 5.0*p_vars["X1"] - 2.0*p_vars["X2"] + residuals


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, tight_layout=True)
ax1.scatter(p_vars["X1"], Y)
ax2.scatter(p_vars["X2"], Y)
ax3.scatter(p_vars["X3"], Y)

ax1.set_title("Y against X1")
ax1.set_xlabel("X1")
ax1.set_ylabel("Y")
ax2.set_title("Y against X2")
ax2.set_xlabel("X2")
ax3.set_title("Y against X3")
ax3.set_xlabel("X3")


plt.show()

model = sm.OLS(Y, p_vars).fit()
print(model.summary())

second_model = sm.OLS(Y, p_vars.loc[:, "const":"X2"]).fit()
print(second_model.summary())