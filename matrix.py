# create a matrix
# any dimension
# multiply 2 matrices
# add 2 matrices
# scale matrix
# create a random mxn matrix
# with values between 0 and 1

from vector import Vector
import random as r


class Matrix:

    def __init__(self, *vec):
        self.matrix = vec
        self.matrix_rows = len(vec)
        self.matrix_cols = len(vec[0])
        pass

    @staticmethod
    def random(row, col):
        v1 = []  # list of numbers
        vec = []
        for _ in range(row):
            for _ in range(col):
                v1.append(r.random())
            vec.append(Vector(*v1))
            v1 = []
        return Matrix(*vec)

    def size(self):
        return "{}x{}".format(self.matrix_rows, self.matrix_cols)

    def __str__(self):
        msg1 = "This is a {} X {} matrix".format(self.matrix_rows, self.matrix_cols)
        msg2 = [x.nums for x in self.matrix]
        return "{} \n {}".format(msg1, msg2)

    def __add__(self, mat):
        return Matrix(*[c1 + c2 for c1, c2 in zip(self.matrix, mat.matrix)])

    def scale(self, scalar):
        return Matrix(*[n.scale(scalar) for n in self.matrix])

        # v1 = Vector(1, 2, 3)
        # v2 = Vector(3, 4, 5)
        # m1 = Matrix(v1, v2)
        # print(m1)
        # print(matrix)
        # m1 = Matrix(matrix)
        # print(m1)
        # for x in m1.matrix[0]:
        #     print(len(x))
        # for x in m1.matrix[0]:
        #     print(x)
    def transpose(self):
        v = []
        m = []
        for col in range(self.matrix_cols):
            for row in self.matrix:
                v.append(row.nums[col])
            m.append(Vector(*v))
            v = []
        return Matrix(*m)

    def mul(self, other):
        t_other = other.transpose()
        v = []
        m = []
        for row in self.matrix:
            for col in t_other.matrix:
                v.append(row.dot(col))
            vec = Vector(*v)
            m.append(vec)
            v = []
        return Matrix(*m)
