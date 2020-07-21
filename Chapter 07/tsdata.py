from collections import deque
import numpy as np
import pandas as pd
import itertools

from numpy.random import default_rng



def _get_n(iterable, n):
    return list(itertools.islice(iterable, n))

def generate_ma(*coeffs, std=1.0, seed=12345):
    rng = default_rng(seed=seed)
    n = len(coeffs)
    past_terms = deque(maxlen=n)
    past_terms.extend([0.0]*n)
    
    coeffs = tuple(reversed(coeffs))

    while True:
        err = rng.normal(0, std)
        yield err + sum(c*e for c, e in zip(coeffs, past_terms))
        past_terms.append(err)

def generate_ar(*coeffs, const=0.0, start=0.0):
    n = len(coeffs)
    past_terms = deque(maxlen=n)
    past_terms.extend([0.0]*(n-1))
    past_terms.append(start)

    coeffs = tuple(reversed(coeffs))

    while True:
        curr = const + sum(c*t for c, t in zip(coeffs, past_terms))
        yield curr
        past_terms.append(curr)


def generate_arma(ar_coeffs=(0.9,), const=0.0, start=0.0, 
                  ma_coeffs=(), noise_std=1.0, seed=None):
    n = len(ar_coeffs)
    past_terms = deque(maxlen=n)
    past_terms.extend([0.0]*(n-1))
    past_terms.append(start)

    coeffs = tuple(reversed(ar_coeffs))

    yield start

    ma_proc = generate_ma(*ma_coeffs, std=noise_std, seed=seed)

    for err in ma_proc:
        curr = const + err + sum(c*t for c, t in zip(coeffs, past_terms))
        yield curr
        past_terms.append(curr)


def undifference(iterable):
    tot = next(iterable)  # first term
    for cur in iterable:
        yield tot
        tot += cur

def add_season_ar(iterable, period=7, coeffs=(0.7,)):
    n = len(coeffs)
    coeffs = tuple(reversed(coeffs))
    N = n + period - 1
    past_vals = deque(maxlen=N)
    past_vals.extend([0.0]*N)

    for item in iterable:
        new = item + sum(coeffs[i]*past_vals[i] for i in range(n))
        yield new
        past_vals.append(new)


def generate_sample_data(train=366, test=50, trend=0.0, undiff=False, seasonal=False):
    gen = generate_arma(seed=12345, const=trend, ar_coeffs=(0.8,), ma_coeffs=(-0.5,))
    
    if seasonal:
        gen = add_season_ar(gen)
    
    if undiff:
        gen = undifference(gen)
    
    indices = pd.date_range("2020-01-01", periods=train+test)
    data = _get_n(gen, train+test)
    return (pd.Series(data[:-test], index=indices[:-test]), 
            pd.Series(data[-test:], index=indices[-test:]))



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    gen = generate_arma(seed=12345, ar_coeffs=(0.9,), ma_coeffs=(-0.5,))
    vals = _get_n(gen, 500)

    plt.plot(vals)
    plt.show()


