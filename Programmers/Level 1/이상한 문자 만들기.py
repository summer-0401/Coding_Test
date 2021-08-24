def solution(s):
    s = s.split()
    return " ".join("".join(chr(ord(x)+(-32,0)[i%2]) for i, x in enumerate(z)) for z in s)

print(solution("try hello world"))