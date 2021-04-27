class agent():
    def __init__(self):
        self.agentLocX = 5
        self.agentLocY = 5
        self.surroundingTerrain = [[0 for i in range(9)] for j in range(9)]
        self.surroundingObjects = [[0 for i in range(9)] for j in range(9)]

    def updateSurroundings(self,typeArray):
        for i in range(0,8):
            self.surroundingTerrain[i] = (typeArray[(self.agentLocX + i - 4)][(self.agentLocY - 4):(self.agentLocY + 4)])
        #print(self.surroundingTerrain)

    def Move(self, direction):
        if direction == 0:
            self.agentLocY += -1
        elif direction == 1:
            self.agentLocX += 1
        elif direction == 2:
            self.agentLocY += 1
        elif direction == 3:
            self.agentLocX += -1