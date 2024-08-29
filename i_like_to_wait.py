import numpy as np
import time

large_matrix = np.random.rand(100, 100)

# It's nice to give the computer a break so it won't get too hot or mad at me
polite_sleep = 10/large_matrix.size

for i in range(100):
    for j in range(100):
        large_matrix[i, j] += np.random.randint(0, 10)
        time.sleep(polite_sleep)

print(large_matrix[0, 0:10])
