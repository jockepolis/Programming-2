"MA4 task 1.1, Monte Carlo Estimation of pi"

import matplotlib.pyplot as plt
import random
import math


fig = plt.figure()
axis = fig.add_subplot(1,1,1)
circle = plt.Circle((0,0), 1)
axis.add_patch(circle)
axis.set_xlim([-1,1])
axis.set_ylim([-1,1])
axis.set_title('A Circle in a Square')


n = 10000
circ = 0
square = 0


for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    dist_origo = x**2 + y**2

    if dist_origo <= 1:
        circ += 1
        plt.plot(x, y, 'ro')
    else:
        plt.plot(x, y, 'go')
    square += 1

pi = 4 * circ/square

print('Number of points in the circle:', circ)
print('Estimation of pi:', pi)
print('"The real pi":', math.pi)
plt.show()