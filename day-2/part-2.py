import re

total = 0

for line in open('input.txt'):
    max = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for round in line.split(';'):
        matches = re.findall(r'(\d+) (red|green|blue)', line)
        for [count, color] in matches:
            if int(count) > max[color]:
                max[color] = int(count)
    total += max['red'] * max['green'] * max['blue']

print(total)
