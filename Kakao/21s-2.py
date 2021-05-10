import numpy as np
from itertools import combinations

def cal(_result, _np_room, a, b, c, d):
    if a<0 or b<0 or c<0 or d<0:
        return _result
    try:
        if _np_room[a][b]=='P' and _np_room[c][d]!='X':
            _result = 0
    except:
        pass

    return _result

def cal2(_result, _np_room, a, b, c, d, e, f):
    if a<0 or b<0 or c<0 or d<0 or e<0 or f<0:
        return _result
    try:
        if _np_room[a][b]=='P' and (_np_room[c][d]!='X' or _np_room[e][f]!='X'):
            _result = 0
    except:
        pass

    return _result

def cal3(_result, _np_room, a, b):
    if a<0 or b<0:
        return _result
    try:
        if _np_room[a][b]=='P':
            _result = 0
    except:
        pass

    return _result

def solution(places):
    answer = []
    
    for room in places:
        result = 1
        for i in range(0,5):
            room[i] = list(room[i])
        np_room = np.array(room)
        np_room = np_room.reshape(5, -1)
        position = np.where(np_room=='P')

        for i, y in enumerate(position[0]):
            x = position[1][i]

            result = cal(result, np_room, y-2, x, y-1, x)
            result = cal(result, np_room, y, x-2, y, x-1)
            result = cal(result, np_room, y+2, x, y+1, x)
            result = cal(result, np_room, y, x+2, y, x+1)
            result = cal2(result, np_room, y-1, x-1, y, x-1, y-1, x)
            result = cal2(result, np_room, y-1, x+1, y, x+1, y-1, x)
            result = cal2(result, np_room, y+1, x-1, y, x-1, y+1, x)
            result = cal2(result, np_room, y+1, x+1, y, x+1, y+1, x)
            result = cal3(result, np_room, y-1, x)
            result = cal3(result, np_room, y, x+1)
            result = cal3(result, np_room, y+1, x)
            result = cal3(result, np_room, y, x+1)
        answer.append(result)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))