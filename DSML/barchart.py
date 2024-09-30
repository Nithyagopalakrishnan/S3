import matplotlib.pyplot as plt
import numpy as np
x = np.array(["Java","Python","PHP","Javascript","C#","C++"])
y = np.array([22.2,17.6,8.8,8,7.7,6.7])
plt.bar(x, y)
plt.xlabel("Programming Language")
plt.ylabel("Popularity")
plt.show()
