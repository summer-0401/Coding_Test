def solution(x, n):
    try:
        return list(range(x, x*(n+1), x))
    except:
        return [x]*n

print(solution(0, 5))