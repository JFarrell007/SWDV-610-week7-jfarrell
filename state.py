"""
Name: Jim Farrell
Description: State class are nodes that will be used in graph.
"""
class State:
    def __init__(self, cLeft,mLeft,direction):
        """constructor initialzied with number of cannibals and missionaries on left and the direction"""
        self.cLeft = cLeft
        self.mLeft = mLeft
        #calculate numbers on the right side of river
        self.cRight = 3 - self.cLeft
        self.mRight = 3 - self.mLeft
        #initial, cross, or return
        self.direction = direction
        
    def getState(self):
        """method to return the state information"""
        return self.cLeft,self.mLeft,self.cRight,self.mRight,self.direction
    
    def getDirection(self):
        """method to return the direction"""
        return self.direction
    
    def isGoal(self):
        """method that checks if the goal is reached.  All parties on right side of river"""
        if self.mLeft == 0 and self.cLeft == 0:
            #print("------------------------------------------DONE----------------------------")
            return True
        return False
    
    def isValidState(self, previous):
        """method that uses previous state and current state to verify if it is a valid transition from one side
           to the other side.
        """
        pcLeft,pmLeft,pcRight,pmRight, pDirection = previous.getState()
        #Each trip of boat needs to be opposite direction from previous crossing
        if pDirection == self.direction:
            return False
        prevL = pcLeft + pmLeft
        curL = self.cLeft + self.mLeft
        prevR = pcRight + pmRight
        curR = self.cRight + self.mRight        
        #May sure the transition never has more than two occupants
        if (((abs(pcLeft - self.cLeft)) + (abs(pmLeft - self.mLeft)) > 2 )):
            return False
        #Always have two people in boat when crossing from left to right
        if(((prevL - curL) != 2) and self.direction == "cross"):           
            return False

        #You can have 1 or 2 occupants on return trip
        if(((curL - prevL) != 1 ) and self.direction == "return"):
            if(pcLeft == 1 and pmLeft == 1 ) and ( self.cLeft == 2 and self.mLeft == 2):
                return True
            return False
        #need to have occupants in the boat
        if((pcLeft == 2 and pmLeft == 2 ) and (self.cLeft == 1 and self.mLeft == 1) and self.direction == "cross"):
            return False     
 
        if self.mLeft >= 0 and self.mRight >= 0 and self.cLeft >= 0 and self.cRight >= 0 and (self.mLeft == 0 or self.mLeft >= self.cLeft) and (self.mRight == 0 or self.mRight >= self.cRight):
            return True
        return False
