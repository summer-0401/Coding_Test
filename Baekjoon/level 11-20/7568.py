from itertools import permutations

n = int(input())
# people 한줄로 입력받기

possibilities = list(permutations(range(n), 2))
rank = [0 for x in range(n)]

for p in possibilities:
    if people[p[0]][0] < people[p[1]][0] and people[p[0]][1] < people[p[1]][1]:
        rank[p[0]]+=1

print(rank)