from numpy import random
import statistics as st
from numpy import random, sqrt, log, sin, cos, pi, argmax
# from RL_Assignment import k_arm_bandit as k
#
#
# for i in range(10):
#     print(random.choice(10))

for i in range(10):
    print(argmax([1,2,3,4,77,3,23,77]))


# def average_reward(rsim):
#     avg_list=[]
#     for i in range(0, 4):
#         temp_list = [rstep[i] for rstep in rsim]
#         step_avg = st.mean(temp_list)
#         avg_list.append(step_avg)
#     return avg_list
#
#
# a=[[1,2,3,4],[1,2,3,8],[1,2,3,4]]
# print(average_reward((a)))




# cnt = {1: 0, 6:0}
# for i in range(10000):
#     cnt[random.choice((1,6),None,False,(.3,.7))] +=1
# print(cnt)


from matplotlib import pyplot as plt

# transformation function
# def gaussian(u1, u2):
#     z1 = sqrt(-2 * log(u1)) * cos(2 * pi * u2)
#     z2 = sqrt(-2 * log(u1)) * sin(2 * pi * u2)
#     return z1, z2
#
# def normal(mean, variance):
#     u1 = random.rand()
#     u2 = random.rand()
#     z1, z2 = gaussian(u1, u2)
#     return mean + (z1 * variance)
#
# m=random.normal(0,1,1000000)
#
# plt.plot(m)
# plt.show()
# plt.hist(m)
# plt.show()

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