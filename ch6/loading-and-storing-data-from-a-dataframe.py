
import pandas as pd
import numpy as np
from numpy.random import default_rng
rng = default_rng(12345)


diffs = rng.normal(0, 1, size=100)
cumulative = np.add.accumulate(diffs)

data_frame = pd.DataFrame({
    "diffs": diffs, 
    "cumulative": cumulative
})
print(data_frame)


data_frame.to_csv("sample.csv", index=False)



df = pd.read_csv("sample.csv", index_col=False)
print(df)
