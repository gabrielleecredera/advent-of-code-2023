import itertools

graph = open('input.txt').read().splitlines()
squares = set()
circles = set()
for y, line in enumerate(graph):
    for x, char in enumerate(line):
        if char == '#':
            squares.add((x, y))
        elif char == 'O':
            circles.add((x, y))
cycle_circles = []
jumped = False
i = 0
for dir in itertools.cycle('NWSE'):
    new_circles = set()
    if dir == 'N':
        top_empty_y = [0] * len(graph[0])
        for y in range(len(graph)):
            for x in range(len(graph[0])):
                if (x, y) in squares:
                    top_empty_y[x] = y + 1
                elif (x, y) in circles:
                    new_circles.add((x, top_empty_y[x]))
                    top_empty_y[x] += 1
    elif dir == 'W':
        for y in range(len(graph)):
            leftmost_empty_x = 0
            for x in range(len(graph[0])):
                if (x, y) in squares:
                    leftmost_empty_x = x + 1
                elif (x, y) in circles:
                    new_circles.add((leftmost_empty_x, y))
                    leftmost_empty_x += 1
    elif dir == 'S':
        bottom_empty_y = [len(graph) - 1] * len(graph[0])
        for y in range(len(graph) - 1, -1, -1):
            for x in range(len(graph[0])):
                if (x, y) in squares:
                    bottom_empty_y[x] = y - 1
                elif (x, y) in circles:
                    new_circles.add((x, bottom_empty_y[x]))
                    bottom_empty_y[x] -= 1
    elif dir == 'E':
        for y in range(len(graph)):
            rightmost_empty_x = len(graph[0]) - 1
            for x in range(len(graph[0]) - 1, -1, -1):
                if (x, y) in squares:
                    rightmost_empty_x = x - 1
                elif (x, y) in circles:
                    new_circles.add((rightmost_empty_x, y))
                    rightmost_empty_x -= 1
    circles = new_circles
    if (i + 1) % 4 == 0 and not jumped:
        if circles in cycle_circles:
            found = (cycle_circles.index(circles) + 1) * 4 - 1
            i = found + (i - found) * ((1000000000 * 4 - 1 - found) // (i - found))
            jumped = True
        cycle_circles.append(circles)
    if i == 1000000000 * 4 - 1:
        break
    i += 1
total = 0
for (_, y) in circles:
    total += len(graph) - y
print(total)
