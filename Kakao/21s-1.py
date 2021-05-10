def solution(s):
    answer = 0
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, n in enumerate(numbers):
        s = s.replace(n, str(i))
    answer = int(s)
    return answer

print(solution("one4seveneight"))