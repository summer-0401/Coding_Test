def solution(s, n):
    s = s.replace('z', '`')
    s = s.replace('Z', '@')
    s = s.split()
    for i, x in enumerate(s):
        s[i]="".join(chr(ord(y)+n) for y in x)
    return " ".join(s)

print(solution("a B z", 4))