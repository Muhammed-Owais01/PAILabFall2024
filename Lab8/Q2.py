import numpy as np

arr = np.arange(1, 19, 2).reshape(3,3)

for i in np.nditer(arr):
    print(i)