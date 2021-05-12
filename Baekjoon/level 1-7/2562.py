a=[]
for i in range(0,9):
    a.append(int(input()))

print(max(a), a.index(max(a))+1, sep="\n")