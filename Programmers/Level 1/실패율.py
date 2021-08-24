def solution(N, stages):
    answer = [[0, 0] for _ in range(N)]
    for s in stages:
        for idx in range(s-1):
            answer[idx][1]+=1
        if s<=N:
            answer[s-1][0]+=1
            answer[s-1][1]+=1
    order = list(range(1, N+1))
    order.sort(key=lambda x: answer[x-1][0]/answer[x-1][1], reverse=True)
    return order

solution(4, [4,4,4,4,4])