graph = open('input.txt').read().splitlines()
visited = {
    ((0, 0), None, 0): 0
}
incomplete = {((0, 0), None, 0)}
target = (len(graph) - 1, len(graph[0]) - 1)
while len(incomplete):
    record, total_cost = min([(i, visited[i]) for i in incomplete], key=lambda x: x[1])
    node, from_node, straight_count = record
    if node == target and straight_count >= 4:
        break
    incomplete.remove(record)
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        neighbour = (node[0] + dy, node[1] + dx)
        if neighbour[0] >= len(graph) or neighbour[0] < 0:
            continue
        if neighbour[1] >= len(graph[0]) or neighbour[1] < 0:
            continue
        is_same_dir = (dy, dx) == (node[0] - from_node[0], node[1] - from_node[1]) if from_node != None else True
        new_straight_count = straight_count + 1 if is_same_dir else 1
        if straight_count < 4 and not is_same_dir:
            continue
        if new_straight_count > 10:
            continue
        if (neighbour, node, new_straight_count) in visited:
            continue
        if from_node != None and (dy == (node[0] - from_node[0]) * -1 and dx == (node[1] - from_node[1]) * -1):
            continue
        new_cost = total_cost + int(graph[neighbour[0]][neighbour[1]])
        new_record = (neighbour, node, new_straight_count)
        visited[new_record] = min(new_cost, visited[new_record] if new_record in visited else 99999999999)
        incomplete.add(new_record)
print(min([visited[i] for i in visited if i[0] == target and i[2] >= 4]))
