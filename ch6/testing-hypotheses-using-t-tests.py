
import pandas as pd
from scipy import stats

sample = pd.Series([
    2.4, 2.4, 2.9, 2.6, 1.8, 2.7, 2.6, 2.4, 2.8, 2.4, 2.4,
    2.4, 2.7, 2.7, 2.3, 2.4, 2.4, 3.2, 2.2, 2.5, 2.1, 1.8,
    2.9, 2.5, 2.5, 3.2, 2. , 2.3, 3. , 1.5, 3.1, 2.5, 3.1,
    2.4, 3. , 2.5, 2.7, 2.1, 2.3, 2.2, 2.5, 2.6, 2.5, 2.8,
    2.5, 2.9, 2.1, 2.8, 2.1, 2.3
])

mu0 = 2.0
significance = 0.05

t_statistic, p_value = stats.ttest_1samp(sample, mu0)

print(f"t stat: {t_statistic}, p value: {p_value}")
# t stat: 9.752368720068665, p value: 4.596949515944238e-13


if p_value <= significance:
    print("Reject H0 in favour of H1: mu != 2.0")
else:
    print("Accept H0: mu = 2.0")
# Reject H0 in favour of H1: mu != 2.0 
