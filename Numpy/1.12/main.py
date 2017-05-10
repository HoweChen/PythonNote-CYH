import numpy
import sys


def numpysum(n):
    a = numpy.arange(n)**2
    b = numpy.arange(n)**3
    c = a + b
    print(c.dtype)
    return c


# size = input("Please input the size")
size = 10
print(numpysum(size))


# multi-dimentional array

m = numpy.array([numpy.arange(size), numpy.arange(size)])
print(m)
print(m.shape)
