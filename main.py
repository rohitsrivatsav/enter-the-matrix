from collections import defaultdict
from functools import reduce

from matrix import Matrix

from vector import Vector

# load matrices from file
vectors = []
matrices = []
with open('matrix.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            matrix = Matrix(*vectors)
            matrices.append(matrix)
            vectors = []
        else:
            vector = Vector(*map(float, line.split(' ')))
            vectors.append(vector)
    matrix = Matrix(*vectors)
    matrices.append(matrix)

# print out all matrices
for i, m in enumerate(matrices):
    print(i, 'matrix:', m.shape, '\n', m, '\n', '-' * 25)

# filter matrices
d = defaultdict(list)
[d[m.shape].append(m) for m in matrices]
print('filtered:', d)

# create 5 3x3 matrices and add together
zero = Vector(0, 0, 0)
final = reduce(lambda acc, mat: acc + mat,
               [Matrix.random(3, 3) for i in range(5)],
               Matrix(zero, zero, zero))
print('final:', final)

# find the dot product of two matrices
dotted = d[(2, 4)][0].dot(d[(4, 2)][0])
print('dotted:', '\n', dotted)
