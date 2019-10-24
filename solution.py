from copy import deepcopy
from sys import stdin


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
        temp = []
        for i in range(len(self.matrix)):
            temp2 = 0
            temp3 = []
            for j in range(len(self.matrix[i])):
                temp2 = float(self.matrix[i][j]) + float(other.matrix[i][j])
                temp3.append(int(temp2))
            temp.append(temp3)
        return Matrix(temp)

    def __mul__(self, k):
        temp = []
        for i in range(len(self.matrix)):
            temp2 = 0
            temp3 = []
            for j in range(len(self.matrix[i])):
                temp3.append(self.matrix[i][j] * k)
            temp.append(temp3)
        return Matrix(temp)

    __rmul__ = __mul__

exec(stdin.read())
