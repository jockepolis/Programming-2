import time

tstart = time.perf_counter()

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(29)

tstop = time.perf_counter()
print (f" Measured time: {tstop - tstart} seconds")