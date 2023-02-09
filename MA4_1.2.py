"MA4 task 1.2, Approximate Volume of d-dimensional Sphere "
"V is dependent of the radius r and has two inputs which is n and d"

import numpy as np
import math
import functools

"Monte Carlo part"

def nSphereVol(d, n):
    in_sphere = 0

    for i in range(n):
        point = np.random.uniform(-1, 1, d)
        distance = lambda point : point**2
        norm = functools.reduce(lambda x,y: x+y,map(distance, point))
        if norm < 1:
            in_sphere += 1

    return np.power(2, d) * (in_sphere / n)


print(nSphereVol(2, 100000))
print(nSphereVol(11, 100000))

"Theoretical part"

def nSphereVolTheo(d):
    V = (math.pi ** (d/2))/(math.gamma((d/2)+1))
    return V

print(nSphereVolTheo(2))
print(nSphereVolTheo(11))

""""

Volume of a ball of radius R is (in this case with R = 1):
When d = 2 --> V = pi * R^2 = pi = 3.14
When d = 11 --> V = (64 * pi^5 / 10395) * R^11 = 1.884 * R^11 = 1.884

"""