import numpy as na
print("enter the size of the array")
n=int(input())
a=[]
for i in range(n):
	x=list(map(int,input().split()))
	a.append(x)
print("Array : ",a)
print("sum of all elements:")
print(na.sum(a))
print("sum of each column:")
print(na.sum(a,axis=0))
print("sum of each row:")
print(na.sum(a,axis=1))
