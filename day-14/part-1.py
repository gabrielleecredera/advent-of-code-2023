top_empty_y = [0] * len(open('input.txt').readline().strip())
total = 0
graph = open('input.txt').read().splitlines()
for y, line in enumerate(graph):
    for x, char in enumerate(line):
        if char == '#':
            top_empty_y[x] = y + 1
        elif char == 'O':
            total += len(graph) - top_empty_y[x]
            top_empty_y[x] += 1
print(total)
