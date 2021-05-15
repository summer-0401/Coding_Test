n, m = map(int, input().split())
lessons = list(map(int, input().split()))

answer = [0 for x in range(m)]
avg = sum(lessons)//m
while lessons:
    if m==1:
        answer[m-1]+=sum(lessons)
        lessons.clear()
    elif abs(avg-(answer[m-1]+lessons[-1])) <= abs(avg-answer[m-1]):
        answer[m-1]+=lessons.pop()
    else:
        avg = sum(lessons)//(m-1)
        m-=1
        answer[m-1]+=lessons.pop()
        if m>len(lessons):
            for j in range(len(lessons)):
                answer[j] += lessons[j]
            break

print(max(answer))