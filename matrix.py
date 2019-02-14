from random import random

from vector import Vector


class Matrix:
    @staticmethod
    def random(rows, cols):
        randrows = [[random() for c in range(cols)] for r in range(rows)]
        return Matrix(*[Vector(*row) for row in randrows])

    def __init__(self, *vectors):
        self.vectors = vectors
        self.shape = (len(vectors), len(vectors[0].nums))

    def __str__(self):
        nl = '\n  '
        return f"[{nl.join([str(v) for v in self.vectors])}]"

    def __add__(self, other):
        if self.shape != other.shape:
            return
        return Matrix(*[self.vectors[row] + other.vectors[row] for row in range(self.shape[0])])

    def scale(self, scalar):
        return Matrix(*[v.scale(scalar) for v in self.vectors])

    def dot(self, other):
        if self.shape != other.shape[::-1]:
            return
        column_vectors = [Vector(*col) for col in zip(*[v.nums for v in other.vectors])]
        transposed = Matrix(*column_vectors)
        vectors = []
        for row in self.vectors:
            nums = []
            for col in transposed.vectors:
                scalar = row.dot(col)
                nums.append(scalar)
            vector = Vector(*nums)
            vectors.append(vector)
        return Matrix(*vectors)
