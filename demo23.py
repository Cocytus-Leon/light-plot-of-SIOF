# %%
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import special
print('Ready!')
# %%


def car2pol(A, B):
    r = np.sqrt(A*A+B*B)
    theta = np.arctan(B/A)
    return r, theta


# %%
a = 5  # * radius of fiber core
x = np.linspace(-a, a, 100)
y = np.linspace(-a, a, 100)
[X, Y] = np.meshgrid(x, y)
r, theta = car2pol(X, Y)
# %%
U = 3.823  # * thansverse propagation constant of fiber core
l = 5  # * order
w = 2  # * width of the light spot
E = sp.special.jv(l, w*U*r/a)/sp.special.jv(l, U)*np.cos(l*theta)
I = E**2
plt.imshow(I)
# %%
