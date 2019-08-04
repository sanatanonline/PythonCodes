import numpy as np

# create a random array
arr = np.random.rand(4, 4)
print(type(arr))
print(arr)

# convert the array to matrix
mat = np.mat(arr)
print(type(mat))
print(mat)

# inverse the matrix
mat_i = mat.I
print(type(mat_i))
print(mat_i)

print(mat*mat_i)
