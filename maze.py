# code adapted from https://www.youtube.com/watch?v=PMMc4VsIacU and
# https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html#mazeSolving and
# https://www.youtube.com/watch?v=Ez7U6jU0q5k 
from cmu_112_graphics import *
import random

class Maze():
    def __init__(self, coordinates, count, rows, cols):
        self.m = [[0] * 10 for row in range(10)]
        self.coordinates = coordinates
        self.count = count
        self.direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.cols = cols
        self.rows = rows

def dfsmaze(rows, cols, x, y):
    finalmaze.m = [[0] * 10 for row in range(10)]
    finalmaze.m[x][y] = 1
    finalmaze.coordinates = (x, y)
    finalmaze.count = 0
    return maze(finalmaze.m, finalmaze.coordinates, finalmaze.count, 
                finalmaze.direction, rows, cols)

def maze(m, coordinates, count, directions, rows, cols):
    board = mazeHelper(m, coordinates, count, directions, rows, cols)
    for x in range(rows):
        for y in range(cols):
            for n in neighbors(x,y):
                j = random.randint(0, 3)
                if isLegal2(n[0], n[1], rows, cols) and clearPath(board, n[0], n[1]):
                    if (board[n[0]][n[1]] == 0 and 
                        (board[n[0]][n[1]] != 0 or (j == 0))):
                        board[n[0]][n[1]] = -1
    
    for x in range(rows):
        for y in range(cols):
            if board[x][y] == 0 and clearPath(board, x, y):
                i = random.randint(0,5)
                if i==0:
                    board[x][y] = -1
    return board

def clearPath(board, x, y):
    if x != 9 and board[x + 1][y] == 1:
        return False
    if x != 0 and board[x - 1][y] == 1:
        return False
    if y != 9 and board[x][y + 1] == 1:
        return False
    if y != 0 and board[x][y - 1] == 1:
        return False
    if x != 9 and y != 9 and board[x + 1][y + 1] == 1:
        return False
    if x != 0 and y != 0 and board[x - 1][y - 1] == 1:
        return False
    if x != 0 and y != 9 and board[x - 1][y + 1] == 1:
        return False
    if x != 9 and y != 0 and board[x + 1][y - 1] == 1:
        return False
    return True

def mazeHelper(m, coordinates, count, directions, rows, cols):
    if finalmaze.coordinates == (rows - 1, cols - 1):
        return m
    else:
        (x, y) = finalmaze.coordinates
        random.shuffle(directions)
        for drow, dcol in directions:
            if isLegal(m, x + drow, y + dcol, rows, cols):
                finalmaze.count += 1
                finalmaze.coordinates = (x + drow, y + dcol)
                finalmaze.m[x + drow][y + dcol] = finalmaze.count
                rest = mazeHelper(m, coordinates, count, directions, rows, cols)
                if rest != None:
                    return rest
                finalmaze.coordinates = (x, y)
                finalmaze.count -= 1
                m[x + drow][y + dcol] = 0
        return None


def neighbors(x, y):
    return [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]


def isLegal(m, currx, curry, rows, cols):
    if currx < 0 or currx >= cols or curry < 0 or curry >= rows:
        return False
    elif m[currx][curry] != 0:
        return False
    return True

def isLegal2(x, y, rows, cols):
    if x < 0 or x >= cols or y < 0 or y >= rows:
        return False
    return True

finalmaze = Maze((0, 0), 1, 10, 10)
dfsmaze(10, 10, 0, 0)
