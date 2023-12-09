total = 0
for line in open('input.txt'):
    layers = [[int(i) for i in line.split(' ')]]
    while any([i != 0 for i in layers[-1]]):
        layers.append([layers[-1][i] - layers[-1][i - 1] for i in range(1, len(layers[-1]))])
    new_value = 0
    for layer in layers[-2::-1]:
        new_value = layer[0] - new_value
    total += new_value
print(total)
