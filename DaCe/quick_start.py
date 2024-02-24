import dace
import numpy as np

@dace.program
def myprogram(a):
    for i in range(a.shape[0]):
        a[i] += i
    return np.sum(a)

print(myprogram(np.array([1,4,8])))