holes = []
for i in range(3):
    input()
    holes.append([int(x) for x in input().split()])

answer=0

for i in range(len(holes[0])):
    for j in range(len(holes[1])):
        for k in range(len(holes[2])):
            if holes[0][i] + holes[2][k] == 2*holes[1][j]:
                answer+=1

print(answer)

#https://suhwanc.tistory.com/163