
import pint


ureg = pint.UnitRegistry(system="mks")


distance = 5280 * ureg.feet
print(distance.to("miles"))
print(distance.to_base_units())
print(distance.to_base_units().to_compact())

@ureg.wraps(ureg.meter, ureg.second)
def calc_depth(dropping_time):
    # s = u*t + 0.5*a*t*t
    # u = 0, a = 9.81
    return 0.5*9.81*dropping_time*dropping_time


depth = calc_depth(0.05 * ureg.minute)
print("Depth", depth)
# Depth 44.144999999999996 meter