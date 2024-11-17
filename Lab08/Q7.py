import numpy as np

arr = np.random.rand(1000)

with open("info.text", "w+") as f:
    f.writelines([
        f"Average: {arr.mean()}\n"
        f"Variance: {arr.var()}\n"
        f"Standard_Deviation: {arr.std()}"
    ])