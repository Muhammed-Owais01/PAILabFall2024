import numpy as np

arr = np.matmul(np.random.choice([2, 5, 9, 10], (4, 4)), np.eye(4))
oddMat = np.arange(1, 33, 2).reshape(4,4)
print(np.add(arr, oddMat))