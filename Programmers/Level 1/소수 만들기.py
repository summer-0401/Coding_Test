from itertools import combinations

def solution(nums):
    answer = 0
    candidates = list(combinations(nums, 3))
    candidates = [sum(x) for x in candidates]

    numbers = list(range(max(candidates)+1))
    numbers[0] = numbers[1] = 0
    for i in range(2, int(max(candidates)**0.5)+1):
        if numbers[i]:
            for j in range(i*i, max(numbers)+1, i):
                numbers[j] = 0

    numbers = [x for x in numbers if x>=2]

    for c in candidates:
        if c in numbers:
            answer+=1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,5,4]))