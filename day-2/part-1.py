import re

max = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

total = 0

for i, line in enumerate(open('input.txt')):
    is_impossible = False
    matches = re.findall(r'(\d+) (red|green|blue)', line)
    for [count, color] in matches:
        if int(count) > max[color]:
            is_impossible = True
    if not is_impossible:
        total += i + 1

print(total)
