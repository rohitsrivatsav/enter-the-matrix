from matrix import Matrix
from vector import Vector
from functools import reduce

# m1 = Matrix.random(3, 4)

# 1 cry
# 2 goto 1
# read in the matrix.txt
# filter the 4x2 and 2x4 matrices into
# different lists

# add any 2 compatible matrices
# multiply any 2 compatible matrices
# scale any matrix
# create a list of 5 3x3 matrices of random values
# and add them together

# multiply a matrix times a vector

with open("matrix.txt") as f:
    vectors = []
    matrix_list = []
    for line in f:
        if(len(line) > 1):
            v = Vector(*tuple(map(int, line.split(' '))))
            vectors.append(v)
            pass
        else:
            m = Matrix(*vectors)
            matrix_list.append(m)
            vectors = []
            pass

    # Seperated lists of 2x4 and 4x2
    matrix_dict = {}
    for m in matrix_list:
        if(m.size() in matrix_dict):
            matrix_dict[m.size()].append(m)
        else:
            matrix_dict[m.size()] = [m]

print(matrix_dict['2x4'][0] + matrix_dict['2x4'][1])
print(Matrix.random(2, 3))
m1 = matrix_dict['2x4'][0]
m2 = matrix_dict['4x2'][0]
# Scale Matrix
m1.scale(3)
# Multiply different size matrix
print(m1.mul(m2))
# print(matrix_dict)
# print(matrix)
# print(matrix[2])
# v = tuple(map(int, rows))
# print(v)
# print(len(rows))
# while len(rows) > 1:
#     print(rows)

# print(v)
mat5 = [Matrix.random(3, 3) for _ in range(5)]
mat_empty = Matrix(*[Vector(0, 0, 0), Vector(0, 0, 0), Vector(0, 0, 0)])
print(reduce(lambda total, mat: total + mat, mat5, mat_empty))
