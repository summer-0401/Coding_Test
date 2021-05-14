def solution(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += hash(part)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(solution(["a","b","c"],["c","a"]))

#https://programmers.co.kr/learn/courses/30/lessons/42576/solution_groups?language=python3 변형