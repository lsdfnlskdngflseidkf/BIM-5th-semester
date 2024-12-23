import numpy as np
import matplotlib.pyplot as plt
randomarray=np.random.randint(1,100,size=10)
randomarray.sort()
squaredarray=np.zeros(10)
i=0;
for element in randomarray:
    squaredarray[i]=element**2
    i+=1
plt.plot(randomarray,label=randomarray,color='blue')
plt.plot(squaredarray,label=squaredarray,color='red')
plt.xlabel("Numbers and their squares")
plt.title("IDK what to put")
plt.show()
