import numpy as na
print("enter the size of the array")
n=int(input())
a=[]
for i in range(n):
	x=list(map(int,input().split()))
	a.append(x)
print("Matrix is : ",a)
print("Inverse of the matrix :")
i=na.linalg.inv(a)
print(i)
