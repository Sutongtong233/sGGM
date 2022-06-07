import numpy as np
A=np.array([[1,2,3],[2,3,4]])
reorder = [1,0]
A=A[reorder][:]
print(A)