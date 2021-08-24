def solution(n, arr1, arr2):
    answer = ['0'*(n-len(bin(a | b)[2:]))+bin(a | b)[2:] for a,b in zip(arr1, arr2)]
    for i, a in enumerate(answer):
        answer[i] = "".join([' ', '#'][int(x)] for x in a)
    return answer

print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))