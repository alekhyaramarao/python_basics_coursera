import matplotlib.pyplot as plt
import numpy


# plt.axis([0,25,0,25])

fig = plt.figure()
ax = fig.gca()
ax.set_xticks(numpy.arange(0, 25, 1))
ax.set_yticks(numpy.arange(0, 25, 1))
plt.plot([2,5,7,8,15,17,20,22],[10,17,3,20,5,23,15,12],'b_',markersize=10)
plt.plot([12,14,15,16,17,18],[14,14.5,13,14,15,14],'g+',markersize=10)
plt.plot(10,4,'ro')

plt.grid()
plt.show()
plt.figure()
