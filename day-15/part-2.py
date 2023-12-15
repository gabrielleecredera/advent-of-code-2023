import collections
import re

sequence = open('input.txt').read().split(',')
boxes = collections.defaultdict(lambda: {})
for text in sequence:
    match = re.match(r'(.+)([=-])(-?\d*)', text)
    value = 0
    for char in match.group(1):
        value += ord(char)
        value *= 17
        value %= 256
    if match.group(2) == '-':
        boxes[value].pop(match.group(1), None)
    elif match.group(2) == '=':
        boxes[value][match.group(1)] = int(match.group(3))

total = 0
for i in boxes:
    for j, slot in enumerate(boxes[i]):
        total += (i + 1) * (j + 1) * (boxes[i][slot])
print(total)
