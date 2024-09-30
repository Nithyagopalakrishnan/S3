import matplotlib.pyplot as plt
x=[]
y=[]
for line in open('sample.txt','r'):
    lines=[i for i in line.split(' ')]
    x.append(lines[0])
    y.append(int(lines[1]))
plt.title("sales and temperature")
plt.xlabel("temperature")
plt.ylabel("sales")
plt.plot(x,y,marker='o',color='g')
pltt.show()
