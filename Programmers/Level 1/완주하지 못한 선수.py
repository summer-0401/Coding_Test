def solution(participant, completion):
    total = sorted(participant+completion)
    for i in range(0,len(total)+1,2):
        try:
            if total[i]!=total[i+1]:
                return total[i]
        except:
            return total[i]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))