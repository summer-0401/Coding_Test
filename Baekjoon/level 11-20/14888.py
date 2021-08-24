from itertools import permutations

n = int(input())
numbers = list(input().split())
add, sub, prd, div = map(int, input().split())
operators = ['+']*add + ['-']*sub + ['*']*prd + ['/']*div

possibles = set(permutations(operators, n-1))

maximum = -1000000001
minimum = 1000000001

for p in possibles:
    candidate = numbers[0]
    for i, op in enumerate(p):
        candidate = '(' + candidate + op + numbers[i+1] + ')'
        if op=='/':#c++의 나눗셈과 python의 // 음수 나눗셈 결과가 다름(ex. -1//3)
            candidate = 'int(' + candidate + ')'
    candidate = eval(candidate)
    maximum = max(maximum, candidate)
    minimum = min(minimum, candidate)

print(maximum, minimum, sep='\n')