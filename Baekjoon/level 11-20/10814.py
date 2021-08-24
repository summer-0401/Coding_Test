import sys
input = sys.stdin.readline #시간 절약
n = int(input())

members = []
for i in range(n):
    a, b = input().split()
    members.append([i, int(a), b])

sorted_members = sorted(members, key=lambda x:(x[1], x[0]))

for m in sorted_members:
    print(m[1], m[2])
