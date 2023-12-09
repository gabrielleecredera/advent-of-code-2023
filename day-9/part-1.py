total = 0
for line in open('input.txt'):
    layers = [[int(i) for i in line.split(' ')]]
    while any([i != 0 for i in layers[-1]]):
        layers.append([layers[-1][i] - layers[-1][i - 1] for i in range(1, len(layers[-1]))])
    total += sum([i[-1] for i in layers])
print(total)
