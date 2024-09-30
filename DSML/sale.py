import matplotlib.pyplot as plt
x=[]
y=[]
f=open("sample3.txt")
next(f)
for row in f:
	row=row.split('	')
	x.append(int(row[0]))
	y.append(int(row[1]))
plt.plot(x,y)
plt.show()	

