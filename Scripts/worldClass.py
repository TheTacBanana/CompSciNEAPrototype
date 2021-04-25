import random, json

class worldMap():
    def __init__(self, size):
        self.arraySize = size
        self.mapArray = [[-1 for i in range(size)] for j in range(size)]

    def shitStartGen(self, x, y):
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

    def genMap(self):
        #for x in range(0,self.arraySize):
        #    self.startGen(x, 0)
        #print(self.mapArray)

        for y in range(0, self.arraySize):
            for x in range(0, self.arraySize):
                if x == 0 and y == 0:
                    self.mapArray[x][y] = round(random.random(),2)
                else:
                    rand = round(random.random(),2)
                    if rand >= 0.1 + self.mapArray[x - 1][y]: #Above
                        rand = 0.1 + self.mapArray[x - 1][y]
                    elif rand <= self.mapArray[x - 1][y] - 0.1: #Below
                        rand = self.mapArray[x - 1][y] - 0.1
                    else:
                        self.mapArray[x][y] = rand                    
