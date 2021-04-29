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

        elif Values > 0 and cols > 0: # Blank Matrix of size x by y
            self.matrixArr = [[0 for i in range(cols)] for j in range(Values)]

        else: # Error Creating Matrix
            raise Exception("Error Creating Matrix")

    def Val(self):
        return self.matrixArr

    def Dimensions(self):
        return [len(self.matrixArr), len(self.matrixArr[0])] # Rows - Columns

    def ScalarMultiply(self, multiplier):
        for y in range(0, len(self.matrixArr)):
            for x in range(0, len(self.matrixArr[0])):
                self.matrixArr[y][x] = self.matrixArr[y][x] * multiplier

    # Basic Matrix Operations
    @staticmethod
    def MatrixAdd(m1, m2): # Dont know how else i would make this more efficient lol
        m1Dims = m1.Dimensions()
        m2Dims = m2.Dimensions()
        if m1Dims[0] != m2Dims[0]:
            raise Exception("Matrices Row Order does not match")
        elif m1Dims[1] != m2Dims[1]:
            raise Exception("Matrices Column Order does not match")
        else:
            newMat = Matrix(m1Dims[0], m1Dims[1])
            for y in range(0, m1Dims[0]):
                for x in range(0, m1Dims[1]):
                    newMat.matrixArr[y][x] = m1.Val()[y][x] + m2.Val()[y][x]
            return newMat

    @staticmethod
    def MatrixMultiply(m1, m2): # Not that efficient, needs optimisation
        m1Dims = m1.Dimensions()
        m2Dims = m2.Dimensions()
        if m1Dims[1] != m2Dims[0]:
            raise Exception("Matrices Multiplication Error")
        else:
            if(type(m2) == Vector):
                newMat = Matrix(m1Dims[0], m2Dims[1])
            else:
                newMat = Matrix(m1Dims[0], m2Dims[1])
            for row in range(0, m1Dims[1]):
                subRow = m1.Val()[row][0:m1Dims[1]]
                for col in range(0, m2Dims[1]):
                    subCol = []
                    for i in range(0, m1Dims[0]):
                        print(i)
                        subCol.append(m2.Val()[i][col])
                    total = 0
                    for x in range(0, len(subRow)):
                        total += subRow[x] * subCol[x]
                    newMat.matrixArr[row][col] = total
            return newMat

class Vector(Matrix):
    def __init__(self, val):
        if type(val) == list:
            if len(val[0]) != 1:
                raise Exception("Invalid Vector, use Matrix Instead")
            else:
                self.matrixArr = val
        else:
            self.matrixArr = [[0 for i in range(1)] for j in range(val)]

    @staticmethod
    def DotProduct(v1,v2):
        if type(v1) != Vector or type(v2) != Vector:
            raise Exception("Wront Types:{},{} passed into Dot Product".format(type(v1),type(v2)))
        else:
            total = 0
            for i in range(v1.Dimensions()[0]):
                total += v1.Val()[i][0] * v2.Val()[i][0]
            return total


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