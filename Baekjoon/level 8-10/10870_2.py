n = int(input())

def line(part1, part2):
    return [''.join(x) for x in zip(part1, part2, part1)]

def stars(_n):
    if _n==1:
        return ['*']

    x = stars(_n//3)
    t_b = line(x, x)
    m = line(x,[' '*(_n//3)]*(_n//3))
    return t_b + m + t_b

print('\n'.join(stars(n)))