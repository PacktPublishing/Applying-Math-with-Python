
from scipy import stats
from numpy.random import default_rng
rng = default_rng(12345)

current = rng.normal(4.0, 2.0, size=40)
process_a = rng.normal(6.2, 2.0, size=25)
process_b = rng.normal(4.5, 2.0, size=64)

significance = 0.05


F_stat, p_value = stats.f_oneway(current, process_b, process_b)

print(f"F stat: {F_stat}, p value: {p_value}")
# F stat: 0.9454281773142474, p value: 0.3906075104622708


if p_value <= significance:
    print("Accept H0: all means equal")
else:
    print("Reject H0: there is a difference between means")
# Reject H0: there is a difference between means