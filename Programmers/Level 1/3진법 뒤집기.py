def solution(n):
    num = ''
    while n>0:
        num += str(n%3)
        n//=3

    num = int(num, 3)
    return num

print(solution(45))
print(solution(125))