def solution(board, moves):
    answer = 0
    board = list(map(lambda x: list(filter(lambda y:y>0, x)), zip(*board)))
    prev=[-1]
    for m in moves:
        if board[m-1]:
            if(collected:=board[m-1].pop(0)) == (prev[-1]):
                answer+=2
                prev.pop()
            else:
                prev.append(collected)
                
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
#참고: https://programmers.co.kr/learn/courses/30/lessons/64061/solution_groups?language=python3