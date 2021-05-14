def solution(nums):
    types = len(set(nums))
    n = len(nums)//2
    return (types if types<n else n)

print(solution([3,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))