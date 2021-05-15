n = int(input())
picture = [[' ' for _ in range(n)] for _ in range(n)]

def stars(y, x, _n):
    if _n==1:
        picture[y][x] = '*'
        return

    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                pass
            else:
                stars(y+i*(_n//3), x+j*(_n//3), _n//3)

stars(0, 0, n)
for i in range(n):
    print(*picture[i],sep="")