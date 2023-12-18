pos = (0, 0)
minx = maxx = miny = maxy = 0
change = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}
walls = {(0, 0)}
for line in open('input.txt').read().splitlines():
    dir, count, _ = line.split(' ')
    count = int(count)
    for i in range(count):
        pos = (pos[0] + change[dir][0], pos[1] + change[dir][1])
        walls.add(pos)
    minx = min(pos[1], minx)
    maxx = max(pos[1], maxx)
    miny = min(pos[0], miny)
    maxy = max(pos[0], maxy)

# known point that's in a lagoon by imagining the input
to_check = {(-1, -4)}
interiors = {(-1, -4)}
while len(to_check):
    pos = to_check.pop()
    for dir in change:
        neighbour = (pos[0] + change[dir][0], pos[1] + change[dir][1])
        if neighbour in walls:
            continue
        if neighbour in interiors:
            continue
        to_check.add(neighbour)
        interiors.add(neighbour)
print(len(interiors) + len(walls))
        