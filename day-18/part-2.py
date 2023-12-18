pos = (0, 0)
change = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}
horizontal_walls = set()
total_wall_count = 0
for line in open('input.txt').read().splitlines():
    _, _, hex = line.split(' ')
    count = int(hex[2: 7], 16)
    total_wall_count += count
    dir = 'RDLU'[int(hex[-2])]
    new_pos = (pos[0] + change[dir][0] * count, pos[1] + change[dir][1] * count)
    if dir == 'L' or dir == 'R':
        horizontal_walls.add((pos, new_pos))
    pos = new_pos

total = 0
on_ranges = []
prev_y = 0
for y in sorted(set([wall[0][0] for wall in horizontal_walls])):
    range_sum = sum([range[1] - range[0] + 1 for range in on_ranges])
    total += (y - prev_y) * range_sum
    prev_y = y
    walls = [wall for wall in horizontal_walls if wall[0][0] == y]
    for wall in walls:
        fromx, tox = sorted([wall[0][1], wall[1][1]])
        overlapping_ranges = [range for range in on_ranges if (range[0] <= fromx <= range[1] or range[0] <= tox <= range[1]) and range[0] != tox and range[1] != fromx]
        # if no overlap or only the one or both ends overlap, switch on
        if not len(overlapping_ranges):
            overlaps = sorted([range for range in on_ranges if range[0] == tox or range[1] == fromx])
            total += tox - fromx  + 1 - len(overlaps)
            if not len(overlaps):
                on_ranges.append((fromx, tox))
            elif len(overlaps) == 1:
                on_ranges.remove(overlaps[0])
                if fromx == overlaps[0][1]:
                    on_ranges.append((overlaps[0][0], tox))
                elif tox == overlaps[0][0]:
                    on_ranges.append((fromx, overlaps[0][1]))
                else:
                    print('WHAT1')
                    exit()
            elif len(overlaps) == 2:
                on_ranges.remove(overlaps[0])
                on_ranges.remove(overlaps[1])
                on_ranges.append((overlaps[0][0], overlaps[1][1]))
        # overlap and not just the ends, switch off
        else:
            if len(overlapping_ranges) > 1:
                print('WHAT2')
                exit()
            overlapping_range = overlapping_ranges[0]
            on_ranges.remove(overlapping_range)
            if overlapping_range[0] == fromx and overlapping_range[1] == tox:
                continue
            elif overlapping_range[0] == fromx:
                on_ranges.append((tox, overlapping_range[1]))
            elif overlapping_range[1] == tox:
                on_ranges.append((overlapping_range[0], fromx))
            elif overlapping_range[0] != fromx and overlapping_range[1] != tox:
                on_ranges.append((tox, overlapping_range[1]))
                on_ranges.append((overlapping_range[0], fromx))
            else:
                print('WHAT3')
                exit()
print(total)

        