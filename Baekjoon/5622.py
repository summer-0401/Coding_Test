word = input()
answer=0

for alphabet in word:
    answer += (3 + (ord(alphabet) - 65)//3)
    if alphabet in 'SVYZ':
        answer-=1

print(answer)