graph = open('input.txt').read().splitlines()
start_y = [y for y, line in enumerate(graph) if 'S' in line][0]
start_pos = (start_y, graph[start_y].index('S'))
queue = {start_pos}
neighbour = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(64):
    new_queue = set()
    for y, x in queue:
        for dy, dx in neighbour:
            new_pos = (y + dy, x + dx)
            if graph[new_pos[0]][new_pos[1]] == '.' or graph[new_pos[0]][new_pos[1]] == 'S':
                new_queue.add(new_pos)
    queue = new_queue
print(len(queue))
