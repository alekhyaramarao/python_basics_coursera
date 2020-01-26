import statistics as st

from numpy import random, sqrt, log, sin, cos, pi
from pylab import show, hist, subplot, figure


# transformation function
def gaussian(u1, u2):
    z1 = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
    z2 = sqrt(-2 * log(u1)) * sin(2 * pi * u2)
    return z1, z2


def normal(mean, sigma, range):
    u1 = random.rand(range)
    u2 = random.rand(range)
    z1, z2 = gaussian(u1, u2)
    return mean + (z1 * sigma)


x = normal(0, 1, 10)

y = []
for i in range(10):
    y.append((normal(0, 10, 10)))

print(y)
print(st.mean(y))
print(st.variance(y))

# plotting the values before and after the transformation
# figure()
#
# subplot(221)  # the first row of graphs
# hist(u1)  # contains the histograms of u1 and u2
# subplot(222)
# hist(u2)
# subplot(223)  # the second contains
# hist(z1)  # the histograms of z1 and z2
# subplot(224)
# hist(z2)
# show()
