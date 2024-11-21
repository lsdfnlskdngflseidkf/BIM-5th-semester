#linestyles change for the gridlines
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
this=np.random.randint(0, 101, size=10)
that=np.random.randint(0, 31, size=10)
this=np.sort(this)
that=np.sort(that)
d1= {'family': 'monospace','color': 'blue', 'size':10}
d2= {'family': 'jetbrains','color': 'blue', 'size':10}

plt.sublplot(1,2,1)
plt.plot(this,that,marker='P',linestyle='-.',color='green',linewidth='1')
plt.xlabel("x axis of the first graph")
plt.ylabel("y axis of first graph") 
plt.title("First subplot")

plt.subplot(1,2,2)
plt.plot(this,that,marker='o',linestyle=':',color='blue',linewidth='1')
plt.xlabel("x axis of the second graph")
plt.ylabel("y axis of second graph") 
plt.title("First subplot")

plt.show()