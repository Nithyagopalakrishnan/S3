import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,6,2,18])
y=np.array([3,12,10,20])
#plt.plot(x,y,ls=':',color='r',marker='o',ms=10,mfc='g',mec='g')
plt.plot(x)
plt.plot(y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(["weight","height"],loc="upper left")
plt.show()
