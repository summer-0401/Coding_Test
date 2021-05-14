import numpy as np

def solution(board, moves):
    answer = 0
    board = np.array(board).T
    prev=[-1]
    for m in moves:
        find = np.where(board[m-1]!=0)
        if find[0]:
            if prev[-1]==board[m-1][find[0][0]]:
                answer+=2
                prev.pop()
            else:
                prev.append(board[m-1][find[0][0]])
            board[m-1][find[0][0]] = 0
                
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))