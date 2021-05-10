def count(anything):
    d = dict()
    for a in anything:
        try:
            d[a]+=1
        except:
            d[a]=1
    return d

def solution(gems):
    answer = [0, 100005]

    total = len(set(gems))
    
    gemMap = dict()

    for i, g in enumerate(gems):
        gemMap[g] = i
        if len(gemMap) == total:
            answer = min(answer,[min(gemMap.values())+1, max(gemMap.values())+1], key=lambda x:(x[1]-x[0],x[0]))

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))