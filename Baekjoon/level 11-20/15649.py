from itertools import permutations

n, m = input().split()

answer = list(permutations(range(1, int(n)+1), int(m)))

for a in answer:
    print(*a)