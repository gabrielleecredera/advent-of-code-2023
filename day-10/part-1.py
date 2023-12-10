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
step = 1
while True:
    step += 1
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
print(step // 2)
