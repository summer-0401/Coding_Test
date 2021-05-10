from itertools import permutations
import re

def cal(nums, ops, rule):
    for operator in rule:
        while True:
            try:
                i = ops.index(operator)
                s = nums.pop(i)+ops.pop(i)+nums.pop(i)
                nums.insert(i, str(eval(s)))

            except:
                break
    return int(nums[0])

def solution(expression):
    answer = 0
    
    #우선순위 규칙
    priorityRule = []
    for i in permutations(['+','-','*']):
        priorityRule.append(list(i))
    
    numbers = re.findall("\d+", expression)
    operators = re.findall("\D", expression)
    for r in priorityRule:
        answer = max(answer, abs(cal(numbers.copy(), operators.copy(), r)))

    return answer

print(solution("2-990-5+2"))