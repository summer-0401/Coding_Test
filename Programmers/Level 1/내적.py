def solution(a, b):
    answer = sum([a[x]*b[x] for x in range(len(a))])
    return answer

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))
