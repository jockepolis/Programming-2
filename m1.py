"""
File m1.py for exam 2022-10-28

Name: Joakim Svensson

"""


import random
import time
import math


#######       A1: depth
def depth(lst):
    if type(lst) is not list:
        return 0
    depth_ = 0
    for item in lst:
        if isinstance(item, list):
            depth_ = max(depth(item), depth_)
    return depth_ + 1

            

#######       A2: is_sorted

def is_sorted(lst):
    if len(lst) < 2:
        return True
    if type(lst[0]) is type(lst[1]):
        return lst[0] <= lst[1] and is_sorted(lst[1:])
    else:
        return False
    


# B1: Time complexity for foo(n)

def foo(n, m=9):
    c = [x for x in range(1, m)]

    def fie(n, c):
        if n == 0:
            return 1
        elif n < 0 or len(c) == 0:
            return 0
        else:
            return fie(n, c[1:]) + fie(n-c[0], c)
    return fie(n, c)


def main():
    print('\n\nA1: depth\n')
    print(f'Result      Argument')
    lists = (1, [], [[]], [1, 2, 3], [[1], 2, [[3]]],
             [[1, (1, [2])], [[[[2]]]], 3], ['[[', [']']])
    for lst in lists:
        print(f'{depth(lst):3d} \t     {str(lst):35}')

    print('\n\nA2: is_sorted\n')
    print('Result       Argument')
    args = ([], [1, 2], [1, 3, 2], [2, 3, 5, 4], ['a', 'ab', 'c'],
            [1, 'a'], [0, False], [[1, 2, 2], [1, 2, 3]])
    for a in args:
        print(f' {is_sorted(a)} \t      {str(a):35}')

    print('\nB1: Timing foo') # Har tagit hjälp av kod från en tidigare tenta där "timing" också används!
    measured = []
    for n in [44,45,46,47,48,49,50]:
        tstart = time.perf_counter()
        print(foo(n), end =' \t')
        dt= time.perf_counter()-tstart
        measured.append(dt)
        print(f"{n} \t {dt}")
        
    for i in range(1,len(measured)):
        print(measured[i]/measured[i-1])
    print(f'Estimation for foo(500): ' +
          f'1.07^450 seconds = 193279687.991 years')


if __name__ == "__main__":
    main()
