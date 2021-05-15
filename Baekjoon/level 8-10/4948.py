while True:
    n = int(input())
    if not n:
        break
    m = 2*n

    numbers = list(range(m+1))
    cnt = n
    for i in range(2, int(m**0.5)+1):
        if numbers[i]:
            for j in range(i*i, max(numbers)+1, i):
                if numbers[j] and j>n:
                    cnt-=1
                numbers[j]=0

    print(cnt)