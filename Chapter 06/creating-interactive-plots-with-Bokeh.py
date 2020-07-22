
import pandas as pd
import numpy as np
from bokeh import plotting as bk
import matplotlib.pyplot as plt

from numpy.random import default_rng
rng = default_rng(12345)

date_range = pd.date_range("2020-01-01", periods=50)
data = np.add.accumulate(rng.normal(0, 3, size=50))
series = pd.Series(data, index=date_range)


bk.output_file("sample.html")

fig = bk.figure(title="Time series data", 
                x_axis_label="date",
                x_axis_type="datetime",
                y_axis_label="value")

fig.line(date_range, series)

bk.show(fig)