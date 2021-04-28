class Matrix():
    def __init__ (self, rows, cols, values = None):
        if values != None:
            self.matrixArr = values
        else:
            self.matrixArr = [[0 for i in range(cols)] for j in range(rows)]

    def val(self):
        return self.matrixArr

    def dimensions(self):
        return [len(self.matrixArr), len(self.matrixArr[0])]

    def scalarMultiply(self, multiplier):
        for y in range(0, len(self.matrixArr)):
            for x in range(0, len(self.matrixArr[0])):
                self.matrixArr[x][y] = self.matrixArr[x][y] * multiplier

# Basic Matrix Operations
def add(m1, m2):
    if m1.dimensions()[0] != m2.dimensions()[0]:
        raise Exception("Matrices Row Order does not match")
    elif m1.dimensions()[1] != m2.dimensions()[1]:
        raise Exception("Matrices Column Order does not match")
    else:
        newMat = Matrix(m1.dimensions()[0], m1.dimensions()[1])
        for y in range(0, m1.dimensions()[0]):
            for x in range(0, m1.dimensions()[1]):
                newMat.matrixArr[x][y] = m1.val()[x][y] + m2.val()[x][y]
        return newMat

def multiply(m1, m2):
    pass
