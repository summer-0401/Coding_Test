from datetime import date
def solution(a, b):
    week_dict = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return week_dict[date(2016, a, b).weekday()]

print(solution(5, 24))