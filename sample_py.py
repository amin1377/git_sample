import os
import time
import numpy
a = numpy.random.rand(1000000)
b = numpy.random.rand(1000000)
tic = time.time()
c = numpy.dot(a, b)
toc = time.time()
print(c)
print(f"numpy func take about {1000 * (toc - tic)} ms")

tic = time.time()
c = 0
for i in range(1000000):
	c += a[i] * b[i]
toc = time.time()
print(c)
print(f"for loop take {1000 * (toc - tic)} ms")
