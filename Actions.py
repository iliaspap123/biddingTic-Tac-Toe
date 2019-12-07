import time
# class Actions(object):
#     """ """

    # def __init__(self):
        # superActions , self).__init__()
        # self.arg = arg

def getSuccessors(currentState,shape):
    succesors = []
    for i in range(3):
        for j in range(3):
            if currentState[i][j] is ' ':
                newState = [x[:] for x in currentState] #copy 2d list
                newState[i][j] = shape
                # print([isSymmetric(newState,previousState) for previousState in succesors])
                if True in [isSymmetric(newState,previousState) for previousState in succesors]:
                    # print(newState,succesors,newState[::-1] == [])
                    continue
                if isWin(newState):
                    succesors.insert(0,newState)
                else:
                    succesors.append(newState)
    return succesors

def isSymmetric(x,y):
    if [r[::-1] for r in x] == y:
        return True
    revx = x[::-1]
    if revx == y:
        return True
    if [r[::-1] for r in revx] == y:
        return True
    tranx = [[x[j][i] for j in range(3)] for i in range(3)]
    if tranx == y:
        return True
    if tranx[::-1] == y:
        return True
    return False



def isWin(listPos):
	for i in range(3):
		if(listPos[i][0] == listPos[i][1] == listPos[i][2] != ' '):
			return(True)
		if(listPos[0][i] == listPos[1][i] == listPos[2][i] != ' '):
			return(True)
	if(listPos[0][0] == listPos[1][1] == listPos[2][2] != ' '):
			return(True)
	if(listPos[0][2] == listPos[1][1] == listPos[2][0] != ' '):
			return(True)
	return(False)

def isFull(listPos):
    for i in range(3):
        for j in range(3):
            if listPos[i][j] == ' ':
                return False
    return True



class MinimaxAgent:
    """
      Your minimax agent (question 2)
    """
    def __init__(self):
        self.tmp1=0
        self.tmp2=0
        self.state = []
        self.sum = 0
    def evaluationFunction(self,listPos,p1):
        eval = 1
        for i in range(3):
            if(listPos[i][0] == listPos[i][1] == listPos[i][2] != ' '):
                if listPos[i][0] == p1:
                    return(0)
                else:
                    return(1)
            if(listPos[0][i] == listPos[1][i] == listPos[2][i] != ' '):
                if listPos[0][i] == p1:
                    return(0)
                else:
                    return(1)
        if(listPos[0][0] == listPos[1][1] == listPos[2][2] != ' '):
            if listPos[0][0] == p1:
                return(0)
            else:
                return(1)
        if(listPos[0][2] == listPos[1][1] == listPos[2][0] != ' '):
            if listPos[0][2] == p1:
                return(0)
            else:
                return(1)
        return eval
    def evaluationFunction2(self,listPos,p1):
        eval = 0
        for i in range(3):
            if(listPos[i][0] == listPos[i][1] == listPos[i][2] != ' '):
                if listPos[i][0] == p1:
                    return(1)
                else:
                    return(-1)
            if(listPos[0][i] == listPos[1][i] == listPos[2][i] != ' '):
                if listPos[0][i] == p1:
                    return(1)
                else:
                    return(-1)
        if(listPos[0][0] == listPos[1][1] == listPos[2][2] != ' '):
            if listPos[0][0] == p1:
                return(1)
            else:
                return(-1)
        if(listPos[0][2] == listPos[1][1] == listPos[2][0] != ' '):
            if listPos[0][2] == p1:
                return(1)
            else:
                return(-1)
        return eval

    def getAction2(self,gameState):
        # if gameState == [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]:
        #     self.tmp1 = 0.359375
        #     self.tmp2 = 0.6796875
        #     self.state = [[' ',' ',' '],[' ','O',' '],[' ',' ',' ']]
        #     return (0.51953125,(1,1))
        def calculateBid(depth,gameState):
            # print(" "*depth,gameState)
            self.sum+=1
            if isFull(gameState) or isWin(gameState) or depth == 9:  # return the utility in case the defined depth is reached or the game is won/lost.
                return self.evaluationFunction(gameState,'O')
            depth += 1
            minR = float("inf")
            sucs = getSuccessors(gameState,'O')
            for nextState in sucs:
                v = calculateBid(depth,nextState)
                if v <= minR:
                    minR = v
                    bestMove = nextState
                    if minR == 0:
                        break

            if minR == 1:
                return 1
            # minR = min(self.calculateBid(depth,nextState) for nextState in )
            # maxR = max(calculateBid(depth,nextState) for nextState in getSuccessors(gameState,'X'))
            maxR = float("-inf")
            sucs = getSuccessors(gameState,'X')
            for nextState in sucs:
                v = calculateBid(depth,nextState)
                if v >= maxR:
                    maxR = v
                    if maxR == 1:
                        break
            self.tmp1 = minR
            self.tmp2 = maxR
            self.state = bestMove
            return abs(minR+maxR) / 2

        res = calculateBid(0,gameState)
        for i in range(3):
            for j in range(3):
                if gameState[i][j] != self.state[i][j]:
                    pos = (i,j)
        # print(res,pos,self.tmp1,self.tmp2)
        return (res,pos)

    def getAction(self, gameState,p1,p2):
        """
          Returns the minimax action from the current gameState using self.depth
        """

        def minimax(agent, depth, gameState,p1,p2):
            #print(gameState)
            if isFull(gameState) or isWin(gameState) or depth == 9:  # return the utility in case the defined depth is reached or the game is won/lost.
                return self.evaluationFunction2(gameState,p1)
            if agent == 0:  # maximize for pacman
                depth += 1
                return sum(minimax(1, depth, nextState,p1,p2) for nextState in getSuccessors(gameState,p1))/len(getSuccessors(gameState,p1))/depth
            else:
                depth += 1
                return sum(minimax(0, depth, nextState,p1,p2) for nextState in getSuccessors(gameState,p2))/len(getSuccessors(gameState,p1))/depth

        """Performing maximize action for the root node i.e. pacman"""
        maximum = float("-inf")
        minimum = float("inf")
        for nextState in getSuccessors(gameState,p1):
            utility = minimax(1, 0, nextState,p1,p2)
            print(nextState,utility)
            if utility > maximum or maximum == float("-inf"):
                maximum = utility
                action = nextState
            # if utility < minimum or minimum == float("inf"):
            #     minimum = utility
            #     action = nextState
        for i in range(3):
            for j in range(3):
                if gameState[i][j] != action[i][j]:
                    pos = (i,j)
        return pos

# cur = [['O','X',' '],[' ','X',' '],[' ','O',' ']]
# sucs = getSuccessors(cur,'X')
# for x in sucs:
#     print(x)

# agent = MinimaxAgent()
# act = agent.getAction(cur,'X','O')
# print(act)
# for i in range(3):
#     for j in range(3):
#         if cur[i][j] != act[i][j]:
#             print(i,j)
# #

# cur = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#
# agent = MinimaxAgent()
# start_time = time.time()
# res = agent.getAction2(cur)
# elapsed_time = time.time() - start_time
#
# print(res)
# print(agent.tmp1,agent.tmp2)
# print(agent.state)
# print("elapsed time is ",elapsed_time)
# print("sum is",agent.sum)
