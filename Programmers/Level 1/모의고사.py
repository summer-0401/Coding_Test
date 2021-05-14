def solution(answers):
    answer =[]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]

    result = {i:0 for i in range(1,4)}

    i = j = k = 0
    for ans in answers:
        if first[i%5] == ans:
            result[1]+=1
        if second[j%8] == ans:
            result[2]+=1
        if third[k%10] == ans:
            result[3]+=1
        i+=1
        j+=1
        k+=1

    win = max(result.values())
    for r in result.keys():
        if result[r]==win:
            answer.append(r)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))