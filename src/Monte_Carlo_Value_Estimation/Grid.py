from numpy import random


class Grid(object):
    def __init__(self, numRows, numColumns, listOfTStates, discountFactor, Policy, transitionProb):
        '''

        :param numRows: Number of Rows for the grid
        :param numColumns: Number of Columns for the grid
        :param listOfTStates: List of States [0,0],[1,2] etc
        :param discountFactor: Value of discount factor for the calculating V(s)
        :param Policy: The name of the text file consisting of Policy given in the format : seperated
        (x(x of state);y(y of state);comma seperated possible actions)
        :param transitionProb: p(s`|s,a)
        '''
        self.numRows = numRows
        self.numColumns = numColumns
        self.listOfTerminalStates = listOfTStates;
        self.returns = [[0 for y in range(self.numColumns)] for x in range(self.numRows)]
        self.numStateVisit = [[0 for y in range(self.numColumns)] for x in range(self.numRows)]
        self.policyGrid = [[() for y in range(self.numColumns)] for x in range(self.numRows)]
        self.discountFactor = discountFactor
        self.policyGrid = self.readPolicy(Policy, self.policyGrid)
        self.transitionProb = transitionProb
        self.trajectoryStates = []
        self.rewardList = []

    def readPolicy(self, PolicyFileName, policyGrid):
        '''
        This method reads the policy file and stores the policy inforamtion in the policy grid.
        Policy grid is initiatlized in the __init__ method og Grid class

        :param PolicyFileName: Name of the Policy File
        :param policyGrid: policy grid of same size as the grid
        :return:
        '''
        file = open(PolicyFileName, "r")
        text = file.read()
        line = text.split(":")
        for obj in line:
            item = obj.split(";")
            policyGrid[int(item[0])][int(item[1])] = list(item[2].split(","))

        return policyGrid

    def getPolicyforState(self, state, PolicyGrid):
        '''
        This method returns the policy(i.e all possible actions) for the given state
        :param state: value of state [x,y]
        :param PolicyGrid: policy grid
        :return: policy for the given state
        '''
        return PolicyGrid[state[0]][state[1]]

    def selectAction(self, state):
        '''
        This methods return the action selected for the given state:
        1.considering equiprobable policy into account for the states having more than one possible actions
        2.considering transition probabilities of selecting correct action i.e p(s`|s,a)
        :param state:value of state [x,y]
        :return: The action selected considering policy and transition probabilities
        '''

        allActions = ['l', 'r', 'u', 'd']
        actionOrder = []
        possibleActions = self.getPolicyforState(state, self.policyGrid)
        equiProb = 1 / len(possibleActions)
        probabilities = [equiProb for i in range(len(possibleActions))]

        policyAction = random.choice(possibleActions, None, False,
                                     (probabilities))  # selects the action as per the given policy
        otherAction = [action for action in allActions if action != policyAction]
        actionOrder.append(policyAction)
        actionOrder = actionOrder + otherAction
        # rearranging actions in a list such that first action has a probability of first item in the transitions probabilities

        return (random.choice((actionOrder), None, False, self.transitionProb))

    def nextState(self, state, action):
        '''
        This method returns the new state for the given action and state
        :param state: Current state [x,y]
        :param action: action taken
        :return: new state as per the action
        '''
        newState = state.copy()
        if action == 'l':
            if (newState[1] - 1 >= 0):
                newState[1] = newState[1] - 1
        elif action == 'r':
            if (newState[1] + 1 < self.numColumns):
                newState[1] = newState[1] + 1
        elif action == 'u':
            if (newState[0] - 1 >= 0):
                newState[0] = newState[0] - 1
        elif action == 'd':
            if (newState[0] + 1 < self.numRows):
                newState[0] = newState[0] + 1

        return newState

    def randomStartState(self):
        x = random.choice([i for i in range(self.numRows)])
        y = random.choice([i for i in range(self.numColumns)])
        return [x, y]

    def trajectoryGenerator(self):
        time = 0
        startState = self.randomStartState()
        if startState not in self.listOfTerminalStates:
            state = startState.copy()
            self.trajectoryStates.append(state)
            while state not in self.listOfTerminalStates:
                state = self.nextState(state, self.selectAction(state)).copy()
                if time > 0:
                    self.rewardList.append(-1)
                self.trajectoryStates.append(state)
                time += 1
            self.rewardList.append(0)

        else:
            self.trajectoryGenerator()

    def valueCalculateFirstVisit(self):
        temp = []
        for state in self.trajectoryStates:
            if state not in temp:
                t = self.trajectoryStates.index(state)
                temp.append(state)
                G = 0
                power = 0
                for i in range(t, len(self.rewardList)):
                    G += self.rewardList[i] * (self.discountFactor ** power)
                    power += 1
                self.returns[state[0]][state[1]] = G
                self.numStateVisit[state[0]][state[1]] += 1

    def valueCalculateEveryVisit(self):
        t=0
        for state in self.trajectoryStates:
            G = 0
            power = 0
            for i in range(t, len(self.rewardList)):
                G += self.rewardList[i] * (self.discountFactor ** power)
                power += 1
            self.returns[state[0]][state[1]] += G
            self.numStateVisit[state[0]][state[1]] += 1
            t+=1

    def createEpisodeFirstVisit(self):
        self.trajectoryGenerator()
        self.valueCalculateFirstVisit()
        return [self.returns,self.numStateVisit]

    def createEpisodeEveryVisit(self):
        self.trajectoryGenerator()
        self.valueCalculateEveryVisit()
        return [self.returns,self.numStateVisit]

    # def valueCalulateEveryVisit(self):








# print(gridWorld.policyGrid)
# print(gridWorld.getPolicyforState((0,3),gridWorld.policyGrid))

# action=[gridWorld.selectAction((0,1)) for i in range(100)]
# print(action.count('l'))
# print(action.count('u'))
# print(action.count('d'))
# print(action.count('r'))
