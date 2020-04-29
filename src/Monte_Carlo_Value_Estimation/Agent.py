from Monte_Carlo_Value_Estimation.Grid import Grid


class Agent(object):
    def __init__(self, numRows, numColumns, listOfTStates, discountFactor, Policy, transitionProb, numEpisodes):
        self.numRows = numRows
        self.numColumns = numColumns
        self.numEpisodes = numEpisodes
        self.listOfTStates = listOfTStates
        self.discountFactor = discountFactor
        self.Policy = Policy
        self.transitionProb = transitionProb
        self.totalReturn = []
        self.numStateVisit = []
        self.avgValue = []


    def initializePlay(self):
        self.totalReturn = [[0 for i in range(self.numColumns)] for j in range(self.numRows)]
        self.numStateVisit = [[0 for i in range(self.numColumns)] for j in range(self.numRows)]
        self.avgValue = [[0 for i in range(self.numColumns)] for j in range(self.numRows)]

    def addMatrix(self, matrixA, matrixB):
        rows = len(matrixA)
        columns = len(matrixA[0])
        sum = [[0 for i in range(columns)] for j in range(rows)]
        for i in range(rows):
            for j in range(columns):
                sum[i][j] = matrixA[i][j] + matrixB[i][j]

        return sum

    def playFirstVisit(self):
        self.initializePlay()
        for i in range(self.numEpisodes):
            grid = Grid(self.numRows, self.numColumns, self.listOfTStates, self.discountFactor, self.Policy,
                        self.transitionProb)
            result = grid.createEpisodeFirstVisit()
            self.totalReturn = self.addMatrix(self.totalReturn, result[0])
            self.numStateVisit = self.addMatrix(self.numStateVisit, result[1])

        for i in range(self.numRows):
            for j in range(self.numColumns):
                if self.numStateVisit[i][j] != 0:
                    self.avgValue[i][j] = self.totalReturn[i][j] / self.numStateVisit[i][j]

        return self.avgValue

    def playEveryVisit(self):
        self.initializePlay()
        for i in range(self.numEpisodes):
            grid = Grid(self.numRows, self.numColumns, self.listOfTStates, self.discountFactor, self.Policy,
                        self.transitionProb)
            result = grid.createEpisodeEveryVisit()
            self.totalReturn = self.addMatrix(self.totalReturn, result[0])
            self.numStateVisit = self.addMatrix(self.numStateVisit, result[1])

        for i in range(self.numRows):
            for j in range(self.numColumns):
                if self.numStateVisit[i][j] != 0:
                    self.avgValue[i][j] = self.totalReturn[i][j] / self.numStateVisit[i][j]

        return self.avgValue


def main():
    numRows = 4
    numColumns = 4
    terminalStates = [[0, 0], [3, 3]]
    discountFactor = 1
    policyFileName = "Policy"
    transitionProbabilities = [0.7, 0.1, 0.1, 0.1]
    numIterations = 4

    agent = Agent(numRows, numColumns, terminalStates, discountFactor, policyFileName, transitionProbabilities,
                  numIterations)
    print(agent.playFirstVisit())
    print(agent.playEveryVisit())


if __name__ == "__main__":
    main()
