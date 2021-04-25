import random

class worldMap():
    def __init__(self, size):
        self.arraySize = size
        self.mapArray = [[-1 for i in range(size)] for j in range(size)]

    def fuckingShittyDepreciatedRecurssion(self, x, y):
        if y == self.arraySize:
            return
        if x == 0:
            self.mapArray[x][y] = round(random.random(),2)
            print(str(x) + " " + str(y) + " " + str(self.mapArray[x][y]))
        else:
            while self.mapArray[x - 1][y] == -1:
                pass
            rand = round(random.random(),2)
            if rand >= 0.1 + self.mapArray[x - 1][y]: #Above
                rand = 0.1 + self.mapArray[x - 1][y]
            elif rand <= self.mapArray[x - 1][y] - 0.1: #Below
                rand = self.mapArray[x - 1][y] - 0.1
            else:
                self.mapArray[x][y] = rand
        
        if x != self.arraySize:
            self.startGen(x, y + 1)

    def genMap(self, seed):
        random.seed(seed)
        for y in range(0, self.arraySize):
            for x in range(0, self.arraySize):
                self.mapArray[x][y] = round(random.random(),2)

        self.smoothGen()

    def smoothGen(self):
        dupMap = self.mapArray
        for y in range(0, self.arraySize):
            for x in range(0, self.arraySize):
                count = 0
                total = 0
                if x != 0 and y != 0:
                    total += dupMap[x - 1][y - 1]
                    count += 1
                if x != 0 and y != self.arraySize - 1:
                    total += dupMap[x - 1][y + 1]
                    count += 1
                if x != self.arraySize - 1 and y != self.arraySize - 1:
                    total += dupMap[x + 1][y + 1]
                    count += 1
                if x != self.arraySize - 1 and y != 0:
                    total += dupMap[x + 1][y - 1]
                    count += 1
                if x != 0:
                    total += dupMap[x - 1][y]
                    count += 1
                if y != 0:
                    total += dupMap[x][y - 1]
                    count += 1
                if x != self.arraySize - 1:
                    total += dupMap[x + 1][y]
                    count += 1
                if y != self.arraySize - 1:
                    total += dupMap[x][y + 1]
                    count += 1

                dupMap[x][y] = total / count
        self.mapArray = dupMap