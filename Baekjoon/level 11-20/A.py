import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

def cal():
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if (a*x + b*y == c) & (d*x + e*y == f):
                print(x, y)
                return

cal()