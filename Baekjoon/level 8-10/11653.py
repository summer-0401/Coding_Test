n = int(input())
numbers = list(range(n+1))

numbers[0] = numbers[1] = 2
for i in range(2, int(n**0.5)+1):
    if numbers[i]:
        for j in range(i*i, max(numbers)+1, i):
            if numbers[j]==j:
                numbers[j] = i

while n>1:
    print(numbers[n])
    n //= numbers[n]