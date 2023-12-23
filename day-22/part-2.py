from collections import defaultdict

bricks = [tuple(map(lambda j: tuple(map(int, j.split(','))), i.split('~'))) for i in open('input.txt').read().splitlines()]
bricks = sorted(bricks, key=lambda i: min(i[0][2], i[1][2]))
max_zs = [[0] * 10 for i in range(10)]
new_bricks = []
for brick in bricks:
    start_x = min(brick[0][0], brick[1][0])
    end_x = max(brick[0][0], brick[1][0]) + 1
    start_y = min(brick[0][1], brick[1][1])
    end_y = max(brick[0][1], brick[1][1]) + 1
    x_max_range = max_zs[brick[0][1]][start_x:end_x]
    y_max_range = [i[brick[0][0]] for i in max_zs][start_y:end_y]
    z_max = max(*x_max_range, *y_max_range)
    new_z_max = z_max + abs(brick[0][2] - brick[1][2]) + 1
    max_zs[brick[0][1]][start_x:end_x] = [new_z_max] * (end_x - start_x)
    for i in range(start_y, end_y):
        max_zs[i][brick[0][0]] = new_z_max
    new_bricks.append(((brick[0][0], brick[0][1], z_max + 1), (brick[1][0], brick[1][1], new_z_max)))

support_map = defaultdict(lambda: [])
for brick in new_bricks:
    start_x = min(brick[0][0], brick[1][0])
    end_x = max(brick[0][0], brick[1][0]) + 1
    start_y = min(brick[0][1], brick[1][1])
    end_y = max(brick[0][1], brick[1][1]) + 1
    z_min = min(brick[0][2], brick[1][2])
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            for other_brick in new_bricks:
                if brick == other_brick:
                    continue
                if max(other_brick[0][2], other_brick[1][2]) != z_min - 1:
                    continue
                if brick in support_map[other_brick]:
                    continue
                other_start_x = min(other_brick[0][0], other_brick[1][0])
                other_end_x = max(other_brick[0][0], other_brick[1][0])
                other_start_y = min(other_brick[0][1], other_brick[1][1])
                other_end_y = max(other_brick[0][1], other_brick[1][1])
                if (other_start_x == x and other_start_y <= y <= other_end_y) or (other_start_y == y and other_start_x <= x <= other_end_x):
                    support_map[other_brick].append(brick)

total = 0
for brick in new_bricks:
    fell_bricks = [brick]
    next_bricks = [i for i in support_map[brick]]
    while len(next_bricks):
        cur_brick = next_bricks.pop(0)
        unmoved_supporters = [i for i, j in support_map.items() if cur_brick in j and i not in fell_bricks]
        if not len(unmoved_supporters) and cur_brick not in fell_bricks:
            fell_bricks.append(cur_brick)
            next_bricks += support_map[cur_brick]
    total += len(fell_bricks) - 1

print(total)
