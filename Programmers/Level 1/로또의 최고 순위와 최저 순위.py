def solution(lottos, win_nums):
    correct = set(lottos) & set(win_nums)
    return [7 - ((len(correct) + lottos.count(0)) or 1), 7 - (len(correct) or 1)]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([1, 2, 5, 6, 7, 8], [20, 9, 3, 45, 4, 35]))