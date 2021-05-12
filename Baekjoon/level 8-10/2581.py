m, n = int(input()), int(input())

numbers = list(range(m,n+1))

if 1 in numbers:
    numbers.remove(1)

if len(numbers)>0:
    for i in range(2,int(max(numbers)**0.5)+1):
        numbers = [x for x in numbers if x==i or x%i!=0]

try:
    r = min(numbers)
    print(sum(numbers))
    print(r)
except:
    print(-1)