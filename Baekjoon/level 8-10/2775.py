t = int(input())
while t:
    answer=0
    t-=1
    k, n = int(input()), int(input())
    apt = []
    apt.append(list(range(n+1)))
    for i in range(1,k):
        apt.append([sum(apt[i-1][:x+1]) for x in range(n+1)])
    print(sum(apt[k-1][:n+1]))