import numpy as np
n=int(input("enter the size of the array"))
arr=[]
for i in range(n):
	x=list(map(int,input().split()))
	arr.append(x)
#print("Matrix is : ",arr)
#print("Inverse of the matrix :")
i=np.transpose(arr)
print(i)
