import sys
input = sys.stdin.readline #시간줄이기

dots = []

n = int(input())
for i in range(n):
    dots.append(list(map(int, input().split())))

dots.sort()
for d in dots:
    print(d[0], d[1])