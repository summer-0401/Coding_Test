input()

xs = list(map(int, input().split()))

xt = list(sorted(set(xs)))
xt = {xt[i]:i for i in range(len(xt))}
print(*[xt[i] for i in xs])