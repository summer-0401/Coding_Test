a=[]
answer = []

a.append(int(input()))
a.append(input())

for i in range(2,-1,-1):
    answer.append(a[0]*int(a[1][i]))

y=0
x=1
for i in answer:
    print(i)
    y+=(i*x)
    x*=10
print(y)