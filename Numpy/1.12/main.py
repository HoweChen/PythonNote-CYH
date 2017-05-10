import numpy
import sys


def numpysum(n):
    a = numpy.arange(n)**2
    b = numpy.arange(n)**3
    c = a + b
    return c


size = input("Please input the size")
print(numpysum(int(size)))
