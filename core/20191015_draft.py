import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b=np.reshape(a, (3,-1))
print(b)
# [[1 2]
#  [3 4]
#  [5 6]]

c=np.reshape(a, (a.size,))
print(c)   # [1 2 3 4 5 6]