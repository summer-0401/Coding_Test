def solution(absolutes, signs):
    values = {True: 1, False: -1}
    return sum(a*values[b] for a, b in zip(absolutes, signs))


print(solution([4,7,12],[True,False,True]))
print(solution([1,2,3], [False,False,True]))