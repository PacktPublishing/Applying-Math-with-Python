
import numpy as np
import scipy as sp

import matplotlib.pyplot as plt


from scipy.stats import beta as beta_dist
beta_pdf = beta_dist.pdf



prior_alpha = 25
prior_beta = 75

args = (prior_alpha, prior_beta)
prior_over_33, err = sp.integrate.quad(beta_pdf, 0.33, 1, args=args)
print("Prior probability", prior_over_33)
# 0.037830787030165056


observed_successes = 122
observed_failures = 257

posterior_alpha = prior_alpha + observed_successes
posterior_beta = prior_beta + observed_failures

args = (posterior_alpha, posterior_beta)
posterior_over_33, err2 = sp.integrate.quad(beta_pdf, 0.33, 1, args=args)
print("Posterior probability", posterior_over_33)
# 0.13686193416281017


p = np.linspace(0, 1, 500)
prior_dist = beta_pdf(p, prior_alpha, prior_beta)
posterior_dist = beta_pdf(p, posterior_alpha, posterior_beta)

fig, ax = plt.subplots()
ax.plot(p, prior_dist, "k--", label="Prior")
ax.plot(p, posterior_dist, "k", label="Posterior")
ax.legend()
ax.set_xlabel("Success rate")
ax.set_ylabel("Density")
ax.set_title("Prior and posterior distributions for success rate")


plt.show()
