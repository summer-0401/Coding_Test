def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]

print(solution([4,3,2,1]))
print(solution([10]))