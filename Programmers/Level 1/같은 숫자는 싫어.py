def solution(arr):
    if not arr:
        return arr
    answer = [arr[0]]
    for x in arr[1:]:
        if answer[-1]!=x:
            answer.append(x)
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))