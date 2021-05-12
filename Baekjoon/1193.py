n = int(input())

i=0
cnt=0
while cnt<n:
    i+=1
    cnt+=i

print("%d/%d"%(1+cnt-n,i-(cnt-n))[::i%2*2-1])