import numpy as np

mat1 = np.random.randint(0, 20, (5, 3))
mat2 = np.random.randint(0, 20, (3, 2))

print(np.matmul(mat1, mat2))