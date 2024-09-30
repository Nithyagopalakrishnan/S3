import numpy as np
array1=list(map(int,input().split()))
array1=np.asarray(array1)
array2=list(map(int,input().split()))
array2=np.asarray(array2)
if np.array_equal(array1,array2):
	print("Equal")
else:
	print("not equal")
