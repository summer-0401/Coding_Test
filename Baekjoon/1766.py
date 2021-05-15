def find(_rule, _n, start):
    while _n[start] in _rule:
        s = _rule[_n[start]].pop(0)
        if len(_rule[_n[start]])==0:
            _rule.pop(_n[start])
        find(_rule, _n, s)
    if (s:=_n[start]):
        print(s, end=" ")
        _n[start]=0
        return
    find(_rule, _n, start)
    return

n, m = map(int, input().split())

priority={}
for i in range(m):
    value, key = map(int, input().split())
    priority[key]=[]
    priority[key].extend([value])

for p in priority:
    priority[p].sort()

n = list(range(n+1))
find(priority, n, 1)