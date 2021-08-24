from itertools import product

m, n = input().split()

answer = product(range(1, int(m)+1), repeat=int(n))

for a in answer:
    print(*a)