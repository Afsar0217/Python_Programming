#Program to show that numpys are faster than Lists
import numpy
import time
size=1000000
list1=[i for i in range(size)]
list2=[i for i in range(size)]
array1=numpy.arange(size)
array2=numpy.arange(size)
initialtime=time.time()
list1=list1+list2
print('Time taken by Lists',(time.time()-initialtime))
initial_time=time.time()
array1=numpy.concatenate((array1,array2),axis=0)
print('Time taken by Arrays',(time.time()-initialtime))

