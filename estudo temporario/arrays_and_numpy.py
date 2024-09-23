import numpy as np

# Exemplo de manipulação de arrays com numpy

# Criar um array a partir de uma lista
array = np.array([1, 2, 3, 4, 5])
print(array[0])
print("Numpy array:", array)  # Output: [1 2 3 4 5]

# Operações básicas com arrays
print("Array + 1:", array + 1)  # Output: [2 3 4 5 6]
print("Array * 2:", array * 2)  # Output: [ 2  4  6  8 10]

# Criar uma matriz (2D array)
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:")
print(matrix)
# Output:
# [[1 2]
#  [3 4]]

# Transpor a matriz
transposed_matrix = matrix.T
print("Transposed matrix:")
print(transposed_matrix)
# Output:
# [[1 3]
#  [2 4]]

x = [1, 2, 3, 4, 5]

a = [n for n in x]
print(a[::2])