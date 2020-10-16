import numpy as np
np.random.seed(101588)

a = 2
b = 4
c = 1
sigma = 4

def true_function(x):
    return a*x**2 + b*x + c


def sample(N):
    x = np.random.randn(N)
    y = true_function(x) + sigma*np.random.randn(N)
    return x, y
