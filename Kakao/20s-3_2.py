def solution(gems):
    total = len(set(gems))
    gemMap = {gems[0]:1}
    tmp = [0, len(gems)-1]
    left, right = 0, 0
    
    while left < len(gems) and right < len(gems):
        if len(gemMap) == total:
            if right - left < tmp[1] - tmp[0]:
                tmp = [left, right]

            gemMap[gems[left]]-=1
            if gemMap[gems[left]]==0:
                del gemMap[gems[left]]

            left+=1

        else:
            right+=1
            if right == len(gems):
                break
            try:
                gemMap[gems[right]]+=1
            except:
                gemMap[gems[right]]=1

    return [tmp[0]+1,tmp[1]+1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))

#참고: https://velog.io/@diddnjs02/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B3%B4%EC%84%9D-%EC%87%BC%ED%95%91
#문제: 효율성 문제 통과 못함