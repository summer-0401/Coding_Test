import numpy as np

def distance(line, board, n):
    try:
        d = board[line].index(1) - line
    except:
        d = n - line
    if d>0:
        d-=1
    else:
        d+=1
    return d

def solution(board):
    answer = 0
    board_t = np.array(board).T.tolist()
    n = len(board)

    x = 0
    y = 0
    prev_x = False
    prev_y = False

    while x!=n-1 or y!=n-1:
        len_x = distance(y, board, n)
        len_y = distance(x, board_t, n)

        if abs(len_x) >= abs(len_y):
            x+=len_x
            answer+=len_x*100
            if prev_y:
                answer+=500
            prev_x=True
            prev_y=False
        
        else:
            y+=len_y
            answer+=len_y*100
            if prev_x:
                answer+=500
            prev_y = True
            prev_x=False
        
    return answer

print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))