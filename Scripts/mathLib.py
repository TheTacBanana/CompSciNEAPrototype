class Matrix():
    def __init__ (self, rows, cols, values = None):
        if values != None:
            self.matrixArr = values
        else:
            self.matrixArr = [[0 for i in range(cols)] for j in range(rows)]

    def val(self):
        return self.matrixArr

    def Dimensions(self):
        return [len(self.matrixArr), len(self.matrixArr[0])] # rows - columns

    def ScalarMultiply(self, multiplier):
        for y in range(0, len(self.matrixArr)):
            for x in range(0, len(self.matrixArr[0])):
                self.matrixArr[y][x] = self.matrixArr[y][x] * multiplier

    # Basic Matrix Operations
    @staticmethod
    def MatrixAdd(m1, m2):
        if m1.dimensions()[0] != m2.dimensions()[0]:
            raise Exception("Matrices Row Order does not match")
        elif m1.dimensions()[1] != m2.dimensions()[1]:
            raise Exception("Matrices Column Order does not match")
        else:
            newMat = Matrix(m1.dimensions()[0], m1.dimensions()[1])
            for y in range(0, m1.dimensions()[0]):
                for x in range(0, m1.dimensions()[1]):
                    newMat.matrixArr[y][x] = m1.val()[y][x] + m2.val()[y][x]
            return newMat

    @staticmethod
    def MatrixMultiply(m1, m2):
        if m1.dimensions()[1] != m2.dimensions()[0]:
            raise Exception("Matrices Multiplication Error")
        else:
            newMat = Matrix(m1.dimensions()[0], m2.dimensions()[1])
            for row in range(0, m1.dimensions()[1]):
                subRow = m1.val()[row][0:m1.dimensions()[1]]
                for col in range(0, m2.dimensions()[0]):
                    subCol = []
                    for i in range(0, m1.dimensions()[0]):
                        subCol.append(m2.val()[i][col])
                    total = 0
                    for x in range(0, len(subRow)):
                        total += subRow[x] * subCol[x]
                    newMat.matrixArr[row][col] = total
            return newMat