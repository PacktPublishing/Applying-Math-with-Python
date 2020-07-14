from uncertainties import ufloat, umath

seconds = ufloat(3.0, 0.4)
print(seconds)  # 3.0+/-0.4


depth = 0.5*9.81*seconds*seconds
print(depth)  # 44+/-12

other_depth = ufloat(44, 12)
time = umath.sqrt(2.0*other_depth/9.81)
print("Estimated time", time)
# Estimated time 3.0+/-0.4

