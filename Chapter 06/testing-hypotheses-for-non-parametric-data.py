
from scipy import stats
from numpy.random import default_rng
rng = default_rng(12345)


sample_A = rng.uniform(2.5, 4.5, size=22)
sample_B = rng.uniform(3.0, 4.4, size=25)
sample_C = rng.uniform(3.0, 4.4, size=30)

significance = 0.05

statistic, p_value = stats.kruskal(sample_A, sample_B, sample_C)
print(f"Statistic: {statistic}, p value: {p_value}")
# Statistic: 5.09365664638392, p value: 0.07832970895845669

if p_value <= significance:
    print("Accept H0: all medians equal")
else:
    print("There are differences between population medians")
# There are differences between population medians

_, p_A_B = stats.ranksums(sample_A, sample_B)
_, p_A_C = stats.ranksums(sample_A, sample_C)
_, p_B_C = stats.ranksums(sample_B, sample_C)

if p_A_B > significance:
    print("Significant differences between A and B, p value", p_A_B)
# Significant differences between A and B, p value 0.08808151166219029


if p_A_C > significance:
    print("Significant differences between A and C, p value", p_A_C)
# Significant differences between A and C, p value 0.4257804790323789

if p_B_C > significance:
    print("Significant differences between B and C, p value", p_B_C)
else:
    print("No significant differences between B and C, p value", p_B_C)
# No significant differences between B and C, p value 0.037610047044153536