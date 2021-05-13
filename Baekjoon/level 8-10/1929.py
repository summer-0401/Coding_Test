m, n = map(int, input().split())

numbers = list(range(n+1))
numbers[0] = numbers[1] = 0
for i in range(2, int(max(numbers)**0.5)+1):
    if numbers[i]:
        for j in range(i*i, max(numbers)+1, i):
            numbers[j] = 0

numbers = [x for x in numbers if x>=m]
print(*numbers,sep="\n",end="")