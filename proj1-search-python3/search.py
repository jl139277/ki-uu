# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from game import Directions
import util
import pdb

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    index = problem.getStartState()
    visitedNodes = [index]
    myPath = []
    hasWon = False
    myStack = util.Stack()

    while not hasWon:
        visitedNodes.append(index)
        for nextNode in problem.getSuccessors(index):
            if nextNode[0] not in visitedNodes:
                myStack.push((nextNode[0], nextNode[1], myPath.copy()))
        value = myStack.pop()
        index = value[0]
        direction = value[1]
        myPath = value[2].copy()
        myPath.append(direction)
        if problem.isGoalState(index):
            hasWon = True

    for x in myPath:
        if x == 'North': x = Directions.NORTH
        if x == 'South': x = Directions.SOUTH
        if x == 'East': x = Directions.EAST
        if x == 'West': x = Directions.WEST
    return myPath

"""def helperFunction(problem, index, direction, cost, path, visited, structure):
    global hasWon
    if index not in visited:
        visited.append(index)
        path.append(direction)
    if problem.isGoalState(index):
        hasWon = True
    for nextNode in problem.getSuccessors(index):
        if nextNode[0] not in visited:
            structure.push((nextNode[0], nextNode[1], nextNode[2], path.copy()))"""

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    index = problem.getStartState()
    visitedNodes = [index]
    myPath = []
    hasWon = False
    myQueue = util.Queue()

    while not hasWon:
        for nextNode in problem.getSuccessors(index):
            if nextNode[0] not in visitedNodes:
                visitedNodes.append((nextNode[0]))
                myQueue.push((nextNode[0], nextNode[1], myPath.copy()))
        value = myQueue.pop()
        index = value[0]
        direction = value[1]
        myPath = value[2].copy()
        myPath.append(direction)
        if problem.isGoalState(index):
            hasWon = True

    for x in myPath:
        if x == 'North': x = Directions.NORTH
        if x == 'South': x = Directions.SOUTH
        if x == 'East': x = Directions.EAST
        if x == 'West': x = Directions.WEST
    return myPath

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    index = problem.getStartState()
    visitedNodes = []
    myPath = []
    hasWon = False
    myPQueue = util.PriorityQueue()

    while not hasWon:
        if index not in visitedNodes:
            visitedNodes.append(index)
            for nextNode in problem.getSuccessors(index):
                if nextNode[0] not in visitedNodes:
                    thisCost = myPath.copy()
                    thisCost.append(nextNode[1])
                    cost = problem.getCostOfActions(thisCost)
                    myPQueue.update((nextNode[0], nextNode[1], myPath.copy()), cost)
        value = myPQueue.pop()
        index = value[0]
        direction = value[1]
        myPath = value[2].copy()
        myPath.append(direction)
        if problem.isGoalState(index):
            hasWon = True

    for x in myPath:
        if x == 'North': x = Directions.NORTH
        if x == 'South': x = Directions.SOUTH
        if x == 'East': x = Directions.EAST
        if x == 'West': x = Directions.WEST
    return myPath


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    index = problem.getStartState()
    visitedNodes = []
    myPath = []
    hasWon = False
    myPQueue = util.PriorityQueue()

    while not hasWon:
        if index not in visitedNodes:
            visitedNodes.append(index)
            for nextNode in problem.getSuccessors(index):
                if nextNode[0] not in visitedNodes:
                    thisCost = myPath.copy()
                    thisCost.append(nextNode[1])
                    cost = problem.getCostOfActions(thisCost)
                    myPQueue.update((nextNode[0], nextNode[1], myPath.copy()), cost + heuristic(nextNode[0], problem))
        value = myPQueue.pop()
        index = value[0]
        direction = value[1]
        myPath = value[2].copy()
        myPath.append(direction)
        if problem.isGoalState(index):
            hasWon = True

    for x in myPath:
        if x == 'North': x = Directions.NORTH
        if x == 'South': x = Directions.SOUTH
        if x == 'East': x = Directions.EAST
        if x == 'West': x = Directions.WEST
    return myPath


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
