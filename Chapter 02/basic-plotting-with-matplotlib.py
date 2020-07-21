
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*(x-2)*np.exp(3 - x)


x = np.linspace(-0.5, 3.0) # 100 values between -0.5 and 3.0
y = f(x)

ax = plt.plot(x, y)
plt.show()

