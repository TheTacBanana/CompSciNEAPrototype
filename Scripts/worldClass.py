import random, json

class worldMap():
    def __init__(self, size):
        self.arraySize = size
        self.heightArray = [[-1 for i in range(size)] for j in range(size)]
        self.colourArray = [[(0, 0, 0) for i in range(size)] for j in range(size)]
        self.typeArray = [[-1 for i in range(size)] for j in range(size)]

        self.inverted = False
        self.grayscale = False
        self.upNeutralDown = 0
        self.averaging = 0
        self.params = []
        self.thresholds = []
        self.loadParameters("DefaultParameters.json")

    def loadParameters(self, fname):
        file = open("Presets\\{}".format(fname), "r")
        self.params = json.loads(file.read())
        file.close()
        
        for key in self.params:
            if key == "Inverted":
                if self.params[key] == 1:
                    self.inverted = True
            elif key == "UpNeutralDown":
                self.upNeutralDown = self.params[key]
            elif key == "Averaging":
                self.averaging = self.params[key]
            elif key == "Grayscale":
                if self.params[key] == 1:
                    self.grayscale = True
            else:
                self.thresholds.append((float(key),(self.params[key][0], self.params[key][1], self.params[key][2])))

    def convertTypes(self):
        for y in range(0, self.arraySize):
            for x in range(0, self.arraySize):
                for i in range(len(self.thresholds)):
                    value = self.heightArray[x][y]
                    if self.inverted:
                        value = 1 - value
                    if value <= self.thresholds[i][0]:
                        #print(thresholds[i][0])
                        self.colourArray[x][y] = self.thresholds[i][1]
                        self.typeArray[x][y] = i
                        break
            

    def genMap(self, seed):
        random.seed(seed)
        for y in range(0, self.arraySize):
            for x in range(0, self.arraySize):
                self.heightArray[x][y] = round(random.random(),2)

        for i in range(self.upNeutralDown):
            self.upNeutralDownGen()
            #print("UNDGen")
        for i in range(self.averaging):
            self.averageGen()
            #print("averaging")       

        self.convertTypes()

    def upNeutralDownGen(self):
        dupMap = self.heightArray
        for y in range(0, self.arraySize):
            for x in range(0, self.arraySize):
                up = 0
                down = 0
                neutral = 0
                pointArr = []

                if x != 0 and y != 0:
                    pointArr.append(self.heightArray[x - 1][y - 1])
                if x != 0 and y != self.arraySize - 1:
                    pointArr.append(self.heightArray[x - 1][y + 1])
                if x != self.arraySize - 1 and y != self.arraySize - 1:
                    pointArr.append(self.heightArray[x + 1][y + 1])
                if x != self.arraySize - 1 and y != 0:
                    pointArr.append(self.heightArray[x + 1][y - 1])
                if x != 0:
                    pointArr.append(self.heightArray[x - 1][y])
                if y != 0:
                    pointArr.append(self.heightArray[x][y - 1])
                if x != self.arraySize - 1:
                    pointArr.append(self.heightArray[x + 1][y])
                if y != self.arraySize - 1:
                    pointArr.append(self.heightArray[x][y + 1])

                for i in range(len(pointArr)):
                    if pointArr[i] >= self.heightArray[x][y] + 0.1:
                        up += 1
                    elif pointArr[i] <= self.heightArray[x][y] - 0.1:
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

        self.heightArray = dupMap

    def averageGen(self):
        dupMap = self.heightArray
        for y in range(0, self.arraySize):
            for x in range(0, self.arraySize):        
                total = 0
                count = 0
                if x != 0 and y != 0:
                    total += self.heightArray[x - 1][y - 1]
                    count += 1
                if x != 0 and y != self.arraySize - 1:
                    total += self.heightArray[x - 1][y + 1]
                    count += 1
                if x != self.arraySize - 1 and y != self.arraySize - 1:
                    total += self.heightArray[x + 1][y + 1]
                    count += 1
                if x != self.arraySize - 1 and y != 0:
                    total += self.heightArray[x + 1][y - 1]
                    count += 1
                if x != 0:
                    total += self.heightArray[x - 1][y]
                    count += 1
                if y != 0:
                    total += self.heightArray[x][y - 1]
                    count += 1
                if x != self.arraySize - 1:
                    total += self.heightArray[x + 1][y]
                    count += 1
                if y != self.arraySize - 1:
                    total += self.heightArray[x][y + 1]
                    count += 1

                dupMap[x][y] = total / count
        self.heightArray = dupMap

    def clamp(self, val, low, high):
        return low if val < low else high if val > high else val