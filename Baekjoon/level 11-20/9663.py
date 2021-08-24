def remove(board, i, j):
    for k in range(n):
        if not board[i][k]:
            board[i][k] = 1
        if not board[k][j]:
            board[k][j] = 1 
    pick = i+j
    for p in range(pick+1):
        if not board[p][pick-p]:
            board[p][pick-p] = 1
    if i<j:
        x = 0
        y = j-i
    else:
        x = i-j
        y = 0
    try:
        for k in range(n):
            if not board[x+k][y+k]:
                board[x+k][y+k] = 1
    except:
        pass

    board[i][j] = 2

n = int(input())

answer = 0

board = []
for i in range(n):
    board.append([0]*n)
for i in range(n):
    for j in range(n):
        if board[i][j]:
            pass
        else:
            remove(board, i, j)

count = sum(x.count(0) for x in board)