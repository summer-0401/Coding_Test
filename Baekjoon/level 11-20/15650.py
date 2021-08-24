from itertools import combinations

m, n = input().split()

answer = combinations(range(1, int(m)+1), int(n))

for a in answer:
    print(*a)