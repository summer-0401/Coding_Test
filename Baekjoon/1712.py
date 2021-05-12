a,b,c = map(int, input().split())

try:
    x = a//(c-b)+1
except:
    x = -1
print(x if x>0 else -1)