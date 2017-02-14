import numpy
import sys


def numpysum(n):
    a = numpy.arange(n)**2
    b = numpy.arange(n)**3
    c = a + b
    return c


size = int(sys.argv[1])
print(numpysum(size))
