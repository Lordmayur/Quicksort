import time
import numpy as np
import matplotlib.pyplot as plt
def partition(templist,low,high):
    i=low-1
    pivot=templist[high]
    for j in range(low,high):
        if templist[j]<=pivot:
            i+=1
            templist[i],templist[j]=templist[j],templist[i]
    templist[i+1],templist[high]=templist[high],templist[i+1]
    return i+1
def quicksort(templist,low,high):
    if low<high:
        pi=partition(templist,low,high)
        quicksort(templist,pi+1,pi-1)
        quicksort(templist,pi+1,high)
elements=np.array([i*1000 for i in range(1,10)])
plt.xlabel("list length")
plt.ylabel("time complexity")
times=[]
for i in range(1,10):
    start=time.time()
    a=np.random.randint(1000,size=i*1000)
    quicksort(a,0,len(a)-1)
    end=time.time()
    times.append(end-start)
    print("quick sort sorted",i*1000,"elements in",end-start,"s")
plt.plot(elements,times,label="quick sort")
plt.grid()
plt.legend()
plt.show()
