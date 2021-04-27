class agent():
    def __init__(self):
        self.agentLoc = (4, 4)
        self.surroundingTerrain = [[0 for i in range(9)] for j in range(9)]
        self.surroundingObjects = [[0 for i in range(9)] for j in range(9)]

    def updateSurroundings(self,typeArray):
        for i in range(0,8):
            self.surroundingTerrain[i] = (typeArray[(self.agentLoc[0] + i - 4)][(self.agentLoc[1] - 4):(self.agentLoc[1] + 4)])
        print(self.surroundingTerrain)

    def Move(self, direction):
        pass