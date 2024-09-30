import numpy as np
print("enter the size of the array")
n=int(input())
arr=[]
for i in range(n):
	x=list(map(int,input().split()))
	arr.append(x)
#print("Matrix is : ",arr)
#print("Inverse of the matrix :")
i=np.linalg.inv(arr)
print(i)
