import math


def findManhattan_h(current,goal,n):
    h = 0
    for i in range(len(current)):
        k = current[i]
        if k != 0:
            index = goal.index(k)
            x1 = i % n
            y1 = i // n
            x2 = index % n
            y2 = index // n
            h = h + abs(x1-x2) + abs(y1-y2)
    return h

def findMisplaced_H(current,goal):
    h=0
    for i in range(len(current)):
        if(current[i] != 0 and (current[i] != goal[i])):
            h = h + 1
    return h

def findMoves(index,n):
    moveList = []
    if(index - n) >= 0:
        moveList.append('up')
    if(index - 1) >=0 and (index + 1)%n != 1:
        moveList.append('left')
    if((index + 1) < n*n) and (index + 1)%n != 0:
        moveList.append('right')
    if(index + n) < n*n:
        moveList.append('down')
    return moveList

def fintNextNodes(moveList,currentNode,index,n,closed):
    nodes = []
    for move in moveList:
        node = list(currentNode)
        newMove = []
        if(move == 'up'):
            newMove = 'UP'
            node[index],node[index-n] = node[index-n],node[index]
        elif(move == 'left'):
            newMove = 'LEFT'
            node[index],node[index-1] = node[index-1],node[index]
        elif(move == 'right'):
            newMove = 'RIGHT'
            node[index],node[index+1] = node[index+1],node[index]
        elif(move == 'down'):
            newMove = 'DOWN'
            node[index],node[index+n] = node[index+n],node[index]
        if(node not in closed):
            nodes.append([node,newMove])
    return nodes

def findNextMove_manhatten(nextNodes, goal, n):
    h = math.inf
    newNode = []
    for nextNode in nextNodes:
        if(findManhattan_h(nextNode[0], goal, n)) < h:
            h = findManhattan_h(nextNode[0], goal, n)
            newNode = nextNode
    return newNode

def findNextMove_misplaced(nextNodes, goal):
    h = math.inf
    newNode = []
    for nextNode in nextNodes:
        if(findMisplaced_H(nextNode[0],goal) < h):
            h = findMisplaced_H(nextNode[0],goal)
            newNode = nextNode
    return newNode

if __name__ == "__main__":
    n= int(input())
    init = []
    for i in range(n*n):
        init.append(int(input()))
    goal = [i for i in range(n*n)]

    

    a = init
    b = goal
    
    openConfig = []
    closed = []
    

    while a != b:
        print(a)
        closed.append(a)
        index = a.index(0)
        moves1 = findMoves(index,n)
        nextNodes1 = fintNextNodes(moves1,a,index,n,closed)
        nextNode = findNextMove_misplaced(nextNodes1, b)
        a = nextNode[0]
        openConfig.append(nextNode[1])

    print (len(openConfig))
    for move in openConfig:
        print(move)