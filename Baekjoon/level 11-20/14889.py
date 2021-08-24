import itertools

n = int(input())

super = []
for _ in range(n):
    super.append(list(map(int, input().split())))

possible = list(itertools.combinations(range(n), n//2))

answer=101
for p in possible[:len(possible)//2+1]:
    combie = list(itertools.permutations(p, 2))
    start = sum(super[x[0]][x[1]] for x in combie)
    other = list(itertools.permutations(set(range(n))-set(p), 2))
    link = sum(super[x[0]][x[1]] for x in other)
    answer = min(abs(start-link), answer)

print(answer)