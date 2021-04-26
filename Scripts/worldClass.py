import random

class worldMap():
    def __init__(self, size):
        self.arraySize = size
        self.mapArray = [[-1 for i in range(size)] for j in range(size)]

    def fuckingShittyDepreciatedRecursion(self, x, y):
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

        self.upNeutralDown()
        self.upNeutralDown()
        self.upNeutralDown()
        self.upNeutralDown()

        self.smoothGen()
        self.smoothGen()
        self.smoothGen()
        self.smoothGen()
        self.smoothGen()
        self.smoothGen()

    def upNeutralDown(self):
        dupMap = self.mapArray
        for y in range(0, self.arraySize):
            for x in range(0, self.arraySize):
                up = 0
                down = 0
                neutral = 0
                pointArr = []

                if x != 0 and y != 0:
                    pointArr.append(self.mapArray[x - 1][y - 1])
                if x != 0 and y != self.arraySize - 1:
                    pointArr.append(self.mapArray[x - 1][y + 1])
                if x != self.arraySize - 1 and y != self.arraySize - 1:
                    pointArr.append(self.mapArray[x + 1][y + 1])
                if x != self.arraySize - 1 and y != 0:
                    pointArr.append(self.mapArray[x + 1][y - 1])
                if x != 0:
                    pointArr.append(self.mapArray[x - 1][y])
                if y != 0:
                    pointArr.append(self.mapArray[x][y - 1])
                if x != self.arraySize - 1:
                    pointArr.append(self.mapArray[x + 1][y])
                if y != self.arraySize - 1:
                    pointArr.append(self.mapArray[x][y + 1])

                for i in range(len(pointArr)):
                    if pointArr[i] >= self.mapArray[x][y] + 0.1:
                        up += 1
                    elif pointArr[i] <= self.mapArray[x][y] - 0.1:
                        down += 1
                    else:
                        neutral += 1

                if (up > down) and (up > neutral): # Up
                    value = 0.09 * up
                elif (down > up) and (down > neutral): # Down
                    value = -0.08 * down
                else: # Neutral
                    value = 0

                dupMap[x][y] += value
                dupMap[x][y] = self.clamp(dupMap[x][y], 0, 1)

        self.mapArray = dupMap

    def smoothGen(self):
        dupMap = self.mapArray
        for y in range(0, self.arraySize):
            for x in range(0, self.arraySize):        
                total = 0
                count = 0
                if x != 0 and y != 0:
                    total += self.mapArray[x - 1][y - 1]
                    count += 1
                if x != 0 and y != self.arraySize - 1:
                    total += self.mapArray[x - 1][y + 1]
                    count += 1
                if x != self.arraySize - 1 and y != self.arraySize - 1:
                    total += self.mapArray[x + 1][y + 1]
                    count += 1
                if x != self.arraySize - 1 and y != 0:
                    total += self.mapArray[x + 1][y - 1]
                    count += 1
                if x != 0:
                    total += self.mapArray[x - 1][y]
                    count += 1
                if y != 0:
                    total += self.mapArray[x][y - 1]
                    count += 1
                if x != self.arraySize - 1:
                    total += self.mapArray[x + 1][y]
                    count += 1
                if y != self.arraySize - 1:
                    total += self.mapArray[x][y + 1]
                    count += 1

                dupMap[x][y] = total / count
        self.mapArray = dupMap

    def clamp(self, val, low, high):
        return low if val < low else high if val > high else val
