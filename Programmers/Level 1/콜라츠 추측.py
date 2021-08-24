def solution(num):
    if num==1:
        return 0
    for i in range(1, 501):
        if (num := [num//2, num*3+1][num & 1]) ==1:
            return i
    return -1

print(solution(1))
print(solution(16))
print(solution(626331))