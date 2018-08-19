import time
import queue
from state import *
from graph import *

class RiverCrossing:
    
    def __init__(self, state):
        """constructor with inital state and graph"""
        self.state = state
        self.graph = Graph()
           
    def getState(self):
        """returns the state of current object"""
        return self.state
    
    def getGraph(self):
        """returns graph object"""
        return self.graph
   
    def get_successors(self, initial):
        """method that iterates through various combinations of state possibilities and
           makes sure they are valid before adding them to the graph"""
        self.graph.addVertex(initial.getState())
        moves = []
        previous = initial
        looking = True
        direction = "cross"
        
        while looking:
            #iterate through the various state combinations
            for can in range(4):
                for mis in range(4):
                    currentState = State(can,mis,direction)
                    #see if the new state is valid if it is add it to the graph
                    if currentState.isValidState(previous):
                        moves.append(currentState)
                        self.graph.addVertex(currentState.getState())
                        self.graph.addEdge(previous.getState(),currentState.getState())
                        previous = currentState
                        if currentState.isGoal():
                            looking = False
            #check to see if you are crossing over return trip and then flip direction
            if direction == "cross":
                direction = "return"
            else:
                direction = "cross"
        return moves

def bfs(g,start):
    """modified book version of breadth first search"""
    start.setDistance(0)
    start.setPred(None)
    vertQueue = queue.Queue(maxsize=0)
    vertQueue.put(start)
    while (not vertQueue.empty()):
        currentVert = vertQueue.get()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.put(nbr)
        currentVert.setColor('black')
                
    
def traverse(y):
    """method from book to travers connections in graph
       currently prints the trip in reverse
    """
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())
    
def printStates(prevMove, curMove):

    cCanLeft,cMisLeft,cCanRight,cMisRight,cDirection = curMove.getState()
    pCanLeft,pMisLeft,pCanRight,pRight,pDirection = prevMove.getState()
    if(cDirection == "cross"):
        print("{} Cannibals and {} Missionaries crossing to destination...{}".format(int(pCanLeft - cCanLeft), int(pMisLeft - cMisLeft), curMove.getState()))
    if(cDirection == "return"):
        print("{} Cannibals and {} Missionaries returning to source.......{}".format(int(cCanLeft - pCanLeft), int(cMisLeft - pMisLeft), curMove.getState()))
        
def runTest():
    #initial state
    initialState = State(3,3,"initial")
    #end state
    endState = State(0,0,"cross")
    initialCrossing = RiverCrossing(initialState)
    #need to come back and remove crossings. Using graph and this can be removed
    crossings = []
    crossings.append(initialCrossing)

    crossings = initialCrossing.get_successors(initialState)
    previousMove = initialCrossing.getState()
    #create the graph 
    graph = initialCrossing.getGraph()

    (bfs(graph,graph.getVertex(initialState.getState())))
    traverse(graph.getVertex(endState.getState()))

    for v in initialCrossing.getGraph().getVertValues():
        for w in v.getConnections():
            print("( %s, %s )" % (v.getId(), w.getId()))
    
    print("{0:>59}{1:>3}{2:>3}{3:>3}".format('C','M','C','M'))
    print("Starting with 3 Cannibals and 3 Missionaries on one side", initialState.getState())
    while crossings:
        currentMove = crossings.pop(0)
        printStates(previousMove, currentMove)
        previousMove = currentMove
        if currentMove.isGoal():
            return currentMove

    
runTest()