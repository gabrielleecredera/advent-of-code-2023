import itertools

map = open('input.txt').read().splitlines()
expand_cols = list(range(0, len(map[0])))
for y, row in  enumerate(map):
    for x in [x for x, i in enumerate(row) if i == '#' and x in expand_cols]:
        expand_cols.remove(x)

dy = 0
galaxies = []
for y, row in enumerate(map):
    dx = 0
    for x, col in enumerate(row):
        if col == '#':
            galaxies.append((y + dy, x + dx))
        if x in expand_cols:
            dx += 1
    if row.count('.') == len(row):
        dy += 1

total = 0
for combination in itertools.combinations(galaxies, 2):
    total += abs(combination[0][0] - combination[1][0]) + abs(combination[0][1] - combination[1][1])
print(total)
