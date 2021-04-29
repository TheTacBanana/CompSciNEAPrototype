import math
class Matrix():
    def __init__ (self, Values, cols = 0, identity = False):
        if type(Values) == list: # Predefined Values
            self.matrixArr = Values
            
        elif identity == True: # Identity Matrix
            if Values != cols:
                raise Exception("Cant create Identity Matrix of different orders")
            else:
                self.matrixArr = [[0 for i in range(cols)] for j in range(Values)]
                for y in range(0, Values):
                    self.matrixArr[y][y] = 1

        else: # Blank Matrix of size x by y
            self.matrixArr = [[0 for i in range(cols)] for j in range(Values)]

    def Val(self):
        return self.matrixArr

    def Dimensions(self):
        return [len(self.matrixArr), len(self.matrixArr[0])] # rows - columns

    def ScalarMultiply(self, multiplier):
        for y in range(0, len(self.matrixArr)):
            for x in range(0, len(self.matrixArr[0])):
                self.matrixArr[y][x] = self.matrixArr[y][x] * multiplier

    # Basic Matrix Operations
    @staticmethod
    def MatrixAdd(m1, m2): # Dont know how else i would make this more efficient lol
        if m1.Dimensions()[0] != m2.Dimensions()[0]:
            raise Exception("Matrices Row Order does not match")
        elif m1.Dimensions()[1] != m2.Dimensions()[1]:
            raise Exception("Matrices Column Order does not match")
        else:
            newMat = Matrix(m1.Dimensions()[0], m1.Dimensions()[1])
            for y in range(0, m1.Dimensions()[0]):
                for x in range(0, m1.Dimensions()[1]):
                    newMat.matrixArr[y][x] = m1.Val()[y][x] + m2.Val()[y][x]
            return newMat

    @staticmethod
    def MatrixMultiply(m1, m2): # Not that efficient, needs optimisation
        if m1.Dimensions()[1] != m2.Dimensions()[0]:
            raise Exception("Matrices Multiplication Error")
        else:
            newMat = Matrix(m1.Dimensions()[0], m2.Dimensions()[1])
            for row in range(0, m1.Dimensions()[1]):
                subRow = m1.Val()[row][0:m1.Dimensions()[1]]
                for col in range(0, m2.Dimensions()[0]):
                    subCol = []
                    for i in range(0, m1.Dimensions()[0]):
                        subCol.append(m2.Val()[i][col])
                    total = 0
                    for x in range(0, len(subRow)):
                        total += subRow[x] * subCol[x]
                    newMat.matrixArr[row][col] = total
            return newMat

class GraphStuff():
    # Constants
    pi = 3.141592653589793
    e = 2.718281828459045

    @staticmethod   # Squishy function
    def Sigmoid(x): 
        return 1/(1 + (GraphStuff().e) ** (-x))

    #Sin Tan Cos
    @staticmethod
    def Sin(x):
        return math.sin(x)
    @staticmethod
    def Cos(x):
        return math.cos(x)
    @staticmethod
    def Tan(x):
        return math.tan(x)