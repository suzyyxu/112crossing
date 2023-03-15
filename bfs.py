#code adapted from https://www.youtube.com/watch?v=U5-bRX2AHNY

board = [[0] * 10 for row in range(10)]
board[0][0] = 1
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

maze = [
[1, 0, -1, 7, 8, 9, 0, -1, -1, -1], 
[1, 2, 3, 6, 11, 10, 0, -1, -1, 0], 
[0, 0, 4, 5, 12, 19, 20, -1, -1, 0], 
[-1, -1, -1, 0, 13, 18, 21, 22, 0, -1], 
[-1, -1, 0, 0, 14, 17, 0, 23, 0, -1], 
[0, -1, -1, -1, 15, 16, 0, 24, -1, -1], 
[-1, -1, -1, -1, -1, 0, 0, 25, -1, -1], 
[0, 0, -1, -1, -1, -1, 0, 26, -1, -1], 
[0, -1, -1, -1, -1, -1, 0, 27, 28, -1], 
[0, -1, -1, 0, 0, 0, -1, 0, 29, 30]]


[[1, 2, 0, 6, 7, 8, 9, 0, 0, 0], 
[2, 3, 4, 5, 6, 7, 8, 0, 0, 0], 
[3, 4, 5, 6, 7, 8, 9, 0, 0, 0], 
[0, 0, 0, 7, 8, 9, 10, 11, 12, 0], 
[0, 0, 9, 8, 9, 10, 11, 12, 13, 0], 
[0, 0, 0, 0, 10, 11, 12, 13, 0, 0], 
[0, 0, 0, 0, 0, 12, 13, 14, 0, 0], 
[0, 0, 0, 0, 0, 0, 14, 15, 0, 0], 
[0, 0, 0, 0, 0, 0, 15, 16, 17, 0], 
[0, 0, 0, 0, 0, 0, 0, 17, 18, 19]]

#i start at 9,9

def bfs(maze, board):
    boardHelper(maze, board)
    # count = board[9][9]
    # path = []
    # countList = []
    # i, j = (9, 9)
    # while (0, 0) not in path:
    #     for drow, dcol in direction:
    #         if inBound(i + drow, i + dcol):
    #             if (board[i + drow][i + dcol] == count and 
    #                 board[i + drow][i + dcol] not in countList):
    #                     countList.append(count)
    #                     path.append((i + drow, j + dcol))
    #     count -= 1
    # return path
    return "done!"

def boardHelper(maze, board):
    level = 1
    while board[9][9] == 0:
        for i in range(10):
            for j in range(10):
                if board[i][j] == level:
                    for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if (inBound(i + x, j + y) and maze[i + x][j + y] != -1 
                            and board[i + x][j + y] == 0):
                            board[i + x][j + y] = level + 1
        level += 1
        

def inBound(x, y):
    if x < 0 or x > 9 or y < 0 or y > 9:
        return False
    return True

print(board)

print(bfs(maze, board))

# class Maze2():
#     def __init__(self, x, y):
#         self.board = [[0] * 10 for row in range(10)]
#         self.path = []
#         self.x = x
#         self.y = y