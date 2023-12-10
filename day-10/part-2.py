# real pipe for start position hard coded in line 62
import re

map = open('input.txt').read().splitlines()
start_y = [i for i, r in enumerate(map) if 'S' in r][0]
prev_pos = (start_y, map[start_y].index('S'))
if map[prev_pos[0]][prev_pos[1] + 1] in '-J7':
    pos = (prev_pos[0], prev_pos[1] + 1)
elif map[prev_pos[0]][prev_pos[1] - 1] in '-LF':
    pos = (prev_pos[0], prev_pos[1] - 1)
elif map[prev_pos[0] + 1][prev_pos[1]] in '|LJ':
    pos = (prev_pos[0] + 1, prev_pos[1])
elif map[prev_pos[0] - 1][prev_pos[1]] in '|F7':
    pos = (prev_pos[0] - 1, prev_pos[1])
next_to_start_pos = pos
walls = {prev_pos}
step = 1
while True:
    step += 1
    walls.add(pos)
    if map[pos[0]][pos[1]] == '|':
        new_pos = (pos[0] - (prev_pos[0] - pos[0]), pos[1])
    elif map[pos[0]][pos[1]] == '-':
        new_pos = (pos[0], pos[1] - (prev_pos[1] - pos[1]))
    elif map[pos[0]][pos[1]] == 'L':
        if prev_pos[0] < pos[0]:
            new_pos = (pos[0], pos[1] + 1)
        else:
            new_pos = (pos[0] - 1, pos[1])
    elif map[pos[0]][pos[1]] == 'J':
        if prev_pos[0] < pos[0]:
            new_pos = (pos[0], pos[1] - 1)
        else:
            new_pos = (pos[0] - 1, pos[1])
    elif map[pos[0]][pos[1]] == '7':
        if prev_pos[0] > pos[0]:
            new_pos = (pos[0], pos[1] - 1)
        else:
            new_pos = (pos[0] + 1, pos[1])
    elif map[pos[0]][pos[1]] == 'F':
        if prev_pos[0] > pos[0]:
            new_pos = (pos[0], pos[1] + 1)
        else:
            new_pos = (pos[0] + 1, pos[1])
    prev_pos, pos = pos, new_pos
    if map[pos[0]][pos[1]] == 'S':
        break
new_map = []
for y in range(len(map)):
    row = []
    for x in range(len(map[0])):
        if (y, x) in walls:
            row.append(map[y][x])
        else:
            row.append('.')
    new_map.append(''.join(row))
count = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if (y, x) in walls:
            continue
        walls_right = len(re.findall(r'F-*J|L-*7|\|', new_map[y][x:].replace('S', 'J')))
        if walls_right % 2 == 1:
            count += 1
print(count)
