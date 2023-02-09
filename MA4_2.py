#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt
import numpy as np


def main():
	NumbaCpp = np.zeros((15, 2))
	f = Person(30)

	for i, j in zip(range(30,45), range(15)):
		f.set(i)
		start_cpp = pc()
		f.fib()
		end_cpp = pc()
		NumbaCpp[j, 0] = end_cpp - start_cpp
		start_numba = pc()
		fib_numba(i)
		end_numba = pc()
		NumbaCpp[j, 1] = end_numba - start_numba

	python = np.zeros((7))
	for i, j in zip(range(30,37), range(7)):
		start_py = pc()
		fib_py(i)
		end_py = pc()
		python[j] = end_py - start_py

	plt.clf()
	plt.plot(range(30,45), NumbaCpp[:, 0], label = "C++")
	plt.plot(range(30,37), python[:], label = "Python")
	plt.plot(range(30,45), NumbaCpp[:, 1], label = "Python x Numba")
	plt.legend()
	plt.savefig("ComparingPythNumbaC++.png")

	PythonNumba = np.zeros((10,2))

	for i, j in zip(range(20,30), range(10)):
		start_py_ = pc()
		fib_py(i)
		end_py_ = pc()
		PythonNumba[j, 0] = end_py_ - start_py_
		start_numba_ = pc()
		fib_numba(i)
		end_numba_ = pc()
		PythonNumba[j, 1] = end_numba_ - start_numba_

	plt.clf()
	plt.plot(range(20,30), PythonNumba[:, 0], label = "Python")
	plt.plot(range(20,30), PythonNumba[:, 1], label = "Numba")
	plt.legend()
	plt.savefig("ComparingPythonNumba.png")
 
def fib_py(f):
	if f <= 1:
		return f
	else:
		return fib_py(f-1) + fib_py(f-2)

@njit
def fib_numba(f):
	if f <= 1:
		return f
	else:
		return (fib_numba(f-1) + fib_numba(f-2))

def CppNumba():
	f = person(47)
	print("C++", f.fib())
	print("Numba", fib_numba(47))

if __name__ == '__main__':
	main()
