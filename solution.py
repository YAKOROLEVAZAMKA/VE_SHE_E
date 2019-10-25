from copy import deepcopy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        temp = ''
        for i in self.matrix:
            for j in i:
                temp = temp + str(j) + '\t'
            temp = temp[:-1]
            temp += '\n'
        temp = temp[:-1]
        return temp

    def size(self):
        return(len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        if (len(self.matrix), len(self.matrix[0])) == (len(other.matrix),
                                                       len(other.matrix[0])):
            temp = []
            for i in range(len(self.matrix)):
                temp2 = 0
                temp3 = []
                for j in range(len(self.matrix[i])):
                    tmp2 = float(self.matrix[i][j]) + float(other.matrix[i][j])
                    temp3.append(int(tmp2))
                temp.append(temp3)
        else:
            error = MatrixError(self, other)
            raise error
        return Matrix(temp)

    def __mul__(self, k):
        temp = []
        for i in range(len(self.matrix)):
            temp3 = []
            for j in range(len(self.matrix[i])):
                temp3.append(self.matrix[i][j] * k)
            temp.append(temp3)
        return Matrix(temp)

    @staticmethod
    def transposed(self):
        temp3 = []
        for i in range(len(self.matrix[0])):
            temp = []
            for j in range(len(self.matrix)):
                temp.append(self.matrix[j][i])
            temp3.append(temp)
        return Matrix(temp3)

    def transpose(self):
        temp3 = []
        for i in range(len(self.matrix[0])):
            temp = []
            for j in range(len(self.matrix)):
                temp.append(self.matrix[j][i])
            temp3.append(temp)
        self.matrix = deepcopy(temp3)
        return Matrix(self.matrix)

    __rmul__ = __mul__

exec(stdin.read())
