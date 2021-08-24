from itertools import combinations_with_replacement

m, n = input().split()

answer = combinations_with_replacement(range(1, int(m)+1), int(n))

for a in answer:
    print(*a)