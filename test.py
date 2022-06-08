import numpy as np
from time import time
A1 = np.random.rand(10, 10)
A2 = np.random.rand(50, 50)
A3 = np.random.rand(100, 100)

t0 = time()
A_1 = np.linalg.inv(A1)
print(time()-t0)
t0 = time()
A_2 = np.linalg.inv(A2)
print(time()-t0)
t0 = time()
A_3 = np.linalg.inv(A3)
print(time()-t0)

