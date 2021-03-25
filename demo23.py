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


def r_over_limit(R):
    A = []
    B = []

    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            if R[i, j] > a:
                A.append(i)
                B.append(j)
    return A, B


# %%
a = 5  # * radius of fiber core
x = np.linspace(-a, a, 100)
y = np.linspace(-a, a, 100)
[X, Y] = np.meshgrid(x, y)
r, theta = car2pol(X, Y)
A, B = r_over_limit(r)
# %%
l = 5  # * order
m = 5  # * number of the mode
# *U: thansverse propagation constant of fiber core
U = (sp.special.jn_zeros(l-1, m)[m-1]+sp.special.jn_zeros(l, m)[m-1])/2
E = sp.special.jv(l, U*r/a)/sp.special.jv(l, U)*np.cos(l*theta)
I = E**2
for k in range(len(A)):
    I[A[k]][B[k]] = 0
plt.imshow(I)
# %%
