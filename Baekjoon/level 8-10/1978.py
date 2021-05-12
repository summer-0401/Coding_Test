n = int(input())

numbers = [int(x) for x in input().split()]

if 1 in numbers:
    numbers.remove(1)

if len(numbers)>0:
    for i in range(2,int(max(numbers)**0.5)+1):
        numbers = [x for x in numbers if x==i or x%i!=0]

print(len(numbers))