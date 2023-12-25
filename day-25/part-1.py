from collections import defaultdict

# just a random node from each group
start = ['jvt', 'qxg']
links = defaultdict(lambda: [])
for line in open('modified-input.txt').read().splitlines():
    from_node, to_nodes = line.split(': ')
    links[from_node] += to_nodes.split(' ')
    for to_node in to_nodes.split(' '):
        links[to_node] += [from_node]

visited = set()
total_a = 0
queue = [start[0]]
while len(queue):
    node = queue.pop(0)
    to_nodes = links[node]
    if node in visited:
        continue
    visited.add(node)
    total_a += 1
    for node in to_nodes:
        queue.append(node)

visited = set()
total_b = 0
queue = [start[1]]
while len(queue):
    node = queue.pop(0)
    to_nodes = links[node]
    if node in visited:
        continue
    visited.add(node)
    total_b += 1
    for node in to_nodes:
        queue.append(node)

print(total_a * total_b)