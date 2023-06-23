import numpy as np
#Slicing Elements of NumpyArray
#Slicing means printing specific elements in a sequencial order...
#[start:stop:step]
a=np.array(['p','y','t','h','o','n'])
print(a[1:5])
print(a[3:])
print(a[4:])
print(a[0:6:2])
print(a[::])      #Prints total Array
print(a[::-1])    #Reverse of given Array
