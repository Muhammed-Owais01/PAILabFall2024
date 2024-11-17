import numpy as np

arr = np.arange(1, 18, 2).reshape(3,3) * 4

newArr = np.matmul(arr, np.eye(3))
print(newArr)