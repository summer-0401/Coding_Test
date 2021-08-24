from itertools import combinations

def solution(numbers):
    possibilities = combinations(numbers, 2)
    answer = set()
    for p in possibilities:
        answer.add(p[0] + p[1])
    return sorted(list(answer))

print(solution([5,0,2,7]))