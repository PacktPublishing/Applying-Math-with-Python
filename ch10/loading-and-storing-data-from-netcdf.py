
import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import default_rng
rng = default_rng(12345)


dates = pd.date_range("2020-01-01", periods=365, name="date")
locations = list(range(25))
steps = rng.normal(0, 1, size=(365,25))
accumulated = np.add.accumulate(steps)

data_array = xr.Dataset({
    "steps": (("date", "location"), steps),
    "accumulated": (("date", "location"), accumulated)
    },
    {"location": locations, "date": dates}
)

print(data_array)
# <xarray.Dataset>
# Dimensions:      (date: 365, location: 25)
# Coordinates:
#   * location     (location) int64 0 1 2 3 4 5 6 7 8 ... 17 18 19 20 21 22 23 24
#   * date         (date) datetime64[ns] 2020-01-01 2020-01-02 ... 2020-12-30
# Data variables:
#     steps        (date, location) float64 -1.424 1.264 ... -0.4547 -0.4873
#     accumulated  (date, location) float64 -1.424 1.264 -0.8707 ... 8.935 -3.525


means = data_array.mean(dim="location")

fig, ax = plt.subplots(tight_layout=True)
means["accumulated"].to_dataframe().plot(ax=ax)
ax.set(title="Mean accumulated values", xlabel="date", ylabel="value")

plt.show()


data_array.to_netcdf("data.nc")


new_data = xr.load_dataset("data.nc")
print(new_data)
# <xarray.Dataset>
# Dimensions:      (date: 365, location: 25)
# Coordinates:
#   * location     (location) int64 0 1 2 3 4 5 6 7 8 ... 17 18 19 20 21 22 23 24
#   * date         (date) datetime64[ns] 2020-01-01 2020-01-02 ... 2020-12-30
# Data variables:
#     steps        (date, location) float64 -1.424 1.264 ... -0.4547 -0.4873
#     accumulated  (date, location) float64 -1.424 1.264 -0.8707 ... 8.935 -3.525