

import numpy as np

def erf_integrand(t):
    return np.exp(-t**2)

from scipy import integrate

val_quad, err_quad = integrate.quad(erf_integrand, -1.0, 1.0) 
# (1.493648265624854, 1.6582826951881447e-14)


val_quadr, err_quadr = integrate.quadrature(erf_integrand, -1.0, 1.0)
# (1.4936482656450039, 7.459897144457273e-10)
