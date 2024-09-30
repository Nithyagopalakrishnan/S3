import matplotlib.pyplot as plt
import numpy as np
mylabel=["Java","Python","PHP","Javascript","C#","C++"]
y = np.array([22.2,17.6,8.8,8,7.7,6.7])
plt.pie(y,labels=mylabel)
plt.show()
