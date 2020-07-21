
import pandas as pd
import numpy as np
from numpy.random import default_rng
rng = default_rng(12345)
three = rng.uniform(-0.2, 1.0, size=100)
three[three < 0] = np.nan

data_frame = pd.DataFrame({
    "one": rng.random(size=100),
    "two": np.add.accumulate(rng.normal(0, 1, size=100)),
    "three": three
})

data_frame["four"] = data_frame["one"] > 0.5

def transform_function(row):
    if row["four"]:
        return 0.5*row["two"]
    return row["one"]*row["two"]

data_frame["five"] = data_frame.apply(transform_function, axis=1)

print(data_frame)


df = data_frame.dropna()

print(df)


