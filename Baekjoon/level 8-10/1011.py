n = int(input())
while n:
    n-=1
    x, y = map(int, input().split())
    print(1 if y-x<=1 else((y-x)))
