r, c = map(int, input().split())
blocks = {'|':[(-1,0),(1,0)], '-':[(0,-1),(0,1)], '+':[(-1,0),(1,0),(0,1),(0,-1)],
    '1':[(1,0),(0,1)], '2':[(-1,0),(0,1)], '3':[(-1,0),(0,-1)], '4':[(0,-1),(1,0)], '.':[]}

plan = []
for i in range(r):
    plan.append(curr:=input())
    if 'M' in curr:
        loc_m = (i,curr.find('M'))
    if 'Z' in curr:
        loc_z = (i,curr.find('Z'))

visiting = [loc_z, loc_m]
visited = [loc_z, loc_m]
while visiting:
    try:
        visit_loc = visiting.pop(1)
    except:
        visit_loc = visiting.pop()
    visit = plan[visit_loc[0]][visit_loc[1]]
    if visit=='Z' or visit=='M':
        for b in blocks['+']:
            try:
                if plan[visit_loc[0]+b[0]][visit_loc[1]+b[1]]!='.':
                   visited.append((visit_loc[0]+b[0],visit_loc[1]+b[1]))
                   visiting.append((visit_loc[0]+b[0],visit_loc[1]+b[1]))
                   break
            except:
                pass
        continue
    if visit=='.':
        blank = visit_loc
        break
    for b in blocks[visit]:
        try:
            if not (s:=(visit_loc[0]+b[0],visit_loc[1]+b[1])) in visited:
                visited.append(s)
                visiting.append(s)
        except:
            pass

print(blank[0]+1,blank[1]+1)