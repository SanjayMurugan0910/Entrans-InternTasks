import numpy as np
# Create arrays
a = np.array([
             [1, 2, 3, 4],
             [1, 2, 3, 4]
             ])
b = np.array([[1, 2], [3, 4]])

# Array attributes
print(a.ndim)      # 1 (dimension)
print(b.shape)     # (2, 2)
print(a.size)      # 4

# Mathematical operations
print(a + 5)       # [6 7 8 9]
print(a * 2)       # [2 4 6 8]
print(np.mean(a))  # 2.5
print(np.sqrt(a))  # [1. 1.414 1.732 2.]

# Random arrays
rand_arr = np.random.randint(1, 10, (3, 3))
print(rand_arr)

# Slicing
print(a[1:3])      # [2 3]
print(b[:, 1])     # Second column → [2 4]
