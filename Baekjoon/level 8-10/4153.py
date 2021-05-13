while True:
    a = [int(x) for x in input().split()]
    if sum(a)==0:
        break
    a.sort()
    print("right" if a[0]**2 + a[1]**2 == a[2]**2 else "wrong")