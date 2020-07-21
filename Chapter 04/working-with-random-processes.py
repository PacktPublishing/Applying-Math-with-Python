import matplotlib.pyplot as plt
import numpy as np

from numpy.random import default_rng
rng = default_rng(12345)

rate = 4.0
inter_arrival_times = rng.exponential(scale=1./rate, size=50)

arrivals = np.add.accumulate(inter_arrival_times)
count = np.arange(50)




fig1, ax1 = plt.subplots()

ax1.step(arrivals, count, where="post")
ax1.set_xlabel("Time")
ax1.set_ylabel("Number of arrivals")
ax1.set_title("Arrivals over time")




from scipy.special import factorial
N = np.arange(15)
def probability(events, time=1, param=rate):
    return ((param*time)**events/factorial(events))*np.exp(-param*time)



fig2, ax2 = plt.subplots()
ax2.plot(N, probability(N), "k", label="True distribution")
ax2.set_xlabel("Number of arrivals in 1 time unit")
ax2.set_ylabel("Probability")
ax2.set_title("Probability distribution")


estimated_scale = np.mean(inter_arrival_times)
estimated_rate = 1.0/estimated_scale


ax2.plot(N, probability(N, param=estimated_rate), "k--", label="Estimated distribution")
ax2.legend()


plt.show()
