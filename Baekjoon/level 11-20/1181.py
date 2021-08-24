words = set()
n = int(input())
for i in range(n):
    words.add(input())
words = list(words)
words.sort(key=lambda x:(len(x), x))

print(*words, sep='\n')