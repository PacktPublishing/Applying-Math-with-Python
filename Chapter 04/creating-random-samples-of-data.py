from numpy.random import default_rng


rng = default_rng(12345)

sample = rng.choice(30, size=5, replace=False)




