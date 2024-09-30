import numpy as np
array1=list(map(int,input().split()))
array1=np.asarray(array1)
array2=list(map(int,input().split()))
array2=np.asarray(array2)
print("Array1:",array1)
print("Array2:",array2)
result=np.multiply(array1,array2)
print("Result is:",result)
