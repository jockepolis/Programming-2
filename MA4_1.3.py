"MA4 task 1.3, Paralell Computing, Approximate Volume of d-dimensional Sphere. "

import numpy as np
import functools
from time import perf_counter as pc
import concurrent.futures as future

"Monte Carlo part"

def nSphereVolume(d, n):
    in_sphere = 0

    for i in range(n):
        point = np.random.uniform(-1, 1, d)
        distance = lambda point : point**2
        norm = functools.reduce(lambda x,y: x+y,map(distance, point))
        if norm < 1:
            in_sphere += 1

    return np.power(2, d) * (in_sphere / n)



if __name__ == "__main__":
    start1 = pc()
    print(nSphereVolume(11,10000000))
    end1 = pc()
    print(f"Process 1 took {round(end1-start1, 2)} seconds")
    start2 = pc()
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(nSphereVolume, [1000000]*10, [11]*10)
    end2 = pc()
    print(f"Process 2 took {round(end2-start2, 2)} seconds")
    
    
""""

10 million points one time took: 74.65 seconds.
1 million points 10 times took: 11.4 seconds.


"""
    
