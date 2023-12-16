graph = open('input.txt').read().splitlines()
start_poses = [((0, -1), (0, 0))]
energized = set()
prev_start_poses = set()
while len(start_poses):
    prev_pos, pos = start_poses.pop()
    while True:
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(graph) or pos[1] >= len(graph[0]):
            break
        if (prev_pos, pos) in prev_start_poses:
            break
        prev_start_poses.add((prev_pos, pos))
        pos_symbol = graph[pos[0]][pos[1]]
        energized.add(pos)
        if pos_symbol == '.' or (pos[0] == prev_pos[0] and pos_symbol == '-') or (pos[1] == prev_pos[1] and pos_symbol == '|'):
            new_pos = (pos[0] + (pos[0] - prev_pos[0]), pos[1] + (pos[1] - prev_pos[1]))
        elif pos_symbol == '\\':
            if pos[0] > prev_pos[0]:
                new_pos = (pos[0], pos[1] + 1)
            elif pos[1] < prev_pos[1]:
                new_pos = (pos[0] - 1, pos[1])
            elif pos[0] < prev_pos[0]:
                new_pos = (pos[0], pos[1] - 1)
            elif pos[1] > prev_pos[1]:
                new_pos = (pos[0] + 1, pos[1])
        elif pos_symbol == '/':
            if pos[0] > prev_pos[0]:
                new_pos = (pos[0], pos[1] - 1)
            elif pos[1] < prev_pos[1]:
                new_pos = (pos[0] + 1, pos[1])
            elif pos[0] < prev_pos[0]:
                new_pos = (pos[0], pos[1] + 1)
            elif pos[1] > prev_pos[1]:
                new_pos = (pos[0] - 1, pos[1])
        elif pos_symbol == '-':
            new_pos = (pos[0], pos[1] - 1)
            start_poses.append((pos, (pos[0], pos[1] + 1)))
        elif pos_symbol == '|':
            new_pos = (pos[0] - 1, pos[1])
            start_poses.append((pos, (pos[0] + 1, pos[1])))
        else:
            print('uh oh')
            exit()
        prev_pos, pos = pos, new_pos
print(len(energized))
